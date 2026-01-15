import streamlit as st
from dotenv import load_dotenv
from gpt import new_application
from cosmos_client import store_gpt_output
load_dotenv()

st.set_page_config(page_title="Azure Advisor", layout="wide")
st.title("Azure Advisor: New vs. Migrate")

if "mode" not in st.session_state:
    st.session_state.mode = None

if "new_suggestions" not in st.session_state:
    st.session_state.new_suggestions = None

if "mig_suggestions" not in st.session_state:
    st.session_state.mig_suggestions = None


col1, col2 = st.columns(2)

with col1:
    if st.button("New Application", type="primary"):
        st.session_state.mode = "new"

with col2:
    if st.button("Migrate to Azure"):
        st.session_state.mode = "migrate"

st.divider()


if st.session_state.mode == "new":
    st.subheader("Design a new application")

    with st.form("new_app_form"):
        app_name = st.text_input("Application Name")
        app_description = st.text_area(
        "Application Description *",
        help="Briefly describe what your application does"
        )

        app_type = st.selectbox(
            "Application Type",
            ["Web App", "API", "Batch Job", "Event-driven", "ML Application"],
        )

        language = st.text_input(
        "Primary Language / Runtime *",
        help="Python, Java, Node.js, .NET, Go" 
        )

        framework = st.text_input("Framework (if applicable)")

        st.subheader("Workload & Scale")

        architecture = st.selectbox(
            "Architecture Style *",
            ["Monolith", "Microservices"]
        )

        state = st.selectbox(
            "Application State *",
            ["Stateless", "Stateful"]
        )

        traffic_rps = st.number_input(
            "Expected Average Requests per Second (RPS) *",
            min_value=1
        )

        autoscaling = st.checkbox(
            "Auto-scaling required",
            value=True
        )

        region_scope = st.selectbox(
            "Deployment Scope *",
            ["Single Region", "Multi Region"]
        )


        st.subheader("Data Requirements")
        with st.expander("Show database options"):

            data_type = st.selectbox(
                "Primary Data Type *",
                ["Relational", "NoSQL", "Blob/Object", "Time-series"]
            )

            data_size_gb = st.number_input(
                "Estimated Data Size (GB) *",
                min_value=1
            )

            read_write_pattern = st.selectbox(
                "Read / Write Pattern *",
                ["Read-heavy", "Write-heavy", "Balanced"]
            )

            schema_flexibility = st.selectbox(
                "Schema Flexibility *",
                ["Low", "Medium", "High"]
            )
    

        st.subheader("Security")
        with st.expander("Security"):
            
            authentication = st.selectbox(
                "Authentication Method *",
                ["Azure AD", "OAuth2", "API Keys"]
            )

            data_sensitivity = st.selectbox(
                "Data Sensitivity Level *",
                ["Public", "Internal", "PII", "PHI"]
            )
            
            st.subheader("Budget")
            monthly_budget = st.number_input(
                "Monthly Budget (USD) *",
                min_value=100
            )

        #submit_new = st.form_submit_button("Get results")

        st.header("Advanced Configuration")
        with st.expander("Show Advanced Options (Optional)"):

            st.subheader("Deployment Preferences")

            deployment_preference = st.selectbox(
                "Deployment Preference",
                ["PaaS Preferred", "IaaS Preferred", "No Preference"]
            )

            custom_os_required = st.checkbox(
                "Requires custom OS or kernel modules"
            )

            legacy_software = st.checkbox(
                "Uses legacy or on-prem dependent software"
            )

            containerization = st.selectbox(
                "Containerization Strategy",
                ["None", "Docker", "Kubernetes"]
            )

            os_type = st.selectbox(
                "Operating System",
                ["Linux", "Windows"]
            )
            # ---------------------------
            # Integration & Messaging
            # ---------------------------
            st.subheader("Integration & Messaging")

            event_driven = st.checkbox("Event-driven architecture")

            message_volume = st.selectbox(
                "Message Volume",
                ["Low", "Medium", "High"]
            )

            external_integrations = st.checkbox(
                "Integrates with external systems / APIs"
            )

            # ---------------------------
            # Security & Compliance (Advanced)
            # ---------------------------
            st.subheader("Security & Compliance")

            compliance = st.multiselect(
                "Compliance Requirements",
                ["GDPR", "HIPAA", "SOC2", "ISO27001"]
            )

            network_isolation = st.checkbox(
                "Require VNET / Private Endpoint"
            )

            # ---------------------------
            # DevOps & Operations
            # ---------------------------
            st.subheader("DevOps & Operations")

            ci_cd = st.selectbox(
                "CI/CD Tool",
                ["GitHub Actions", "Azure DevOps", "Other"]
            )

            environment_count = st.number_input(
                "Number of Environments (Dev/Test/Prod)",
                min_value=1,
                max_value=5,
                value=3
            )

            uptime_sla = st.selectbox(
                "Target SLA",
                ["99.9", "99.99", "99.999"]
            )

            # ---------------------------
            # Cost Optimization
            # ---------------------------
            st.subheader("Cost Optimization")

            cost_priority = st.selectbox(
                "Cost Optimization Priority",
                ["Low", "Medium", "High"]
            )
        submit_new = st.form_submit_button("Get results")

    if submit_new:
        payload = {
            "app_metadata": {
            "name": app_name,
            "description": app_description,
            "type": app_type,
            "language": language,
            "framework": framework
            },
            "workload": {
                "architecture": architecture,
                "state": state,
                "traffic_rps": traffic_rps,
                "autoscaling": autoscaling,
                "region_scope": region_scope
            },
            "data": {
                "data_type": data_type,
                "data_size_gb": data_size_gb,
                "read_write_pattern": read_write_pattern,
                "schema_flexibility": schema_flexibility
            },
            "security": {
                "authentication": authentication,
                "data_sensitivity": data_sensitivity,
                "compliance": compliance,
                "network_isolation": network_isolation
            },
            "deployment": {
                "preference": deployment_preference,
                "custom_os_required": custom_os_required,
                "legacy_software": legacy_software,
                "containerization": containerization,
                "os_type": os_type
            },
            "integration": {
                "event_driven": event_driven,
                "message_volume": message_volume,
                "external_integrations": external_integrations
            },
            "devops": {
                "ci_cd": ci_cd,
                "environment_count": environment_count,
                "uptime_sla": uptime_sla
            },
            "cost": {
                "monthly_budget_usd": monthly_budget,
                "cost_priority": cost_priority
            }
        }

        st.session_state.new_payload = payload

        with st.spinner("Calling GPT 5.2-chat(Azure Foundry)..."):
            try:
                st.session_state.new_suggestions = new_application(payload)
            except Exception as e:
                st.error(f"GPT call failed: {e}")
                st.stop()
        store_gpt_output(st.session_state.new_payload, st.session_state.new_suggestions)

    # ---------------------------
    # SHOW SUGGESTIONS
    # ---------------------------
    if st.session_state.new_suggestions:
        titles = [
            s.get("title", f"Option {i+1}")
            for i, s in enumerate(st.session_state.new_suggestions)
        ]

        choice = st.radio("Choose a suggestion", titles)

        selected = st.session_state.new_suggestions[titles.index(choice)]
        st.json(selected)
    
        
