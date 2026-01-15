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
    
        
if st.session_state.mode == "migrate":
    st.subheader("Migrate Existing Application to Azure")

    with st.form("migrate_app_form"):
        # ---------------------------
        # Application Profile
        # ---------------------------
        st.subheader("Application Profile")

        app_name = st.text_input("Application Name")
        application_size = st.selectbox(
            "Application Size",
            ["Small", "Medium", "Large"]
        )

        application_type = st.selectbox(
            "Application Type",
            ["Monolith", "Microservices", "SOA"]
        )

        statefulness = st.selectbox(
            "Application State",
            ["Stateless", "Stateful"]
        )

        # ---------------------------
        # Technology Stack
        # ---------------------------
        st.subheader("Technology Stack")

        frontend_tech = st.text_input("Frontend Technology")
        backend_tech = st.text_input("Backend Technology")
        middleware_used = st.text_input("Middleware (e.g. MQ, Kafka, ESB)")
        database_engine = st.selectbox(
            "Database Engine",
            ["SQL Server", "Oracle", "MySQL", "PostgreSQL", "MongoDB", "Other"]
        )

        # ---------------------------
        # Compute & Hosting
        # ---------------------------
        st.subheader("Compute & Hosting")

        hosting_preference = st.selectbox(
            "Preferred Azure Hosting",
            ["VM", "App Service", "AKS", "No Preference"]
        )

        os_type = st.selectbox(
            "Operating System",
            ["Linux", "Windows"]
        )

        containerized = st.checkbox("Currently Containerized")

        # ---------------------------
        # Data & Storage
        # ---------------------------
        st.subheader("Data")

        data_size_gb = st.number_input(
            "Total Data Size (GB)",
            min_value=1
        )

        backup_required = st.checkbox("Backup Required")

        # ---------------------------
        # Security & Identity
        # ---------------------------
        st.subheader("Security")

        auth_method = st.selectbox(
            "Authentication Method",
            ["Basic Auth", "LDAP", "SSO", "OAuth"]
        )

        compliance = st.multiselect(
            "Compliance Requirements",
            ["GDPR", "HIPAA", "SOC2", "ISO27001"]
        )

        # ---------------------------
        # Connectivity
        # ---------------------------
        st.subheader("Connectivity")

        end_user_client = st.selectbox(
            "End User Client",
            ["Browser", "Desktop", "Mobile", "API"]
        )

        network_port = st.number_input(
            "Exposed Network Port",
            value=443
        )

        external_dependency = st.checkbox(
            "External / 3rd Party Integrations"
        )

        # ---------------------------
        # Operations
        # ---------------------------
        st.subheader("Operations")

        background_jobs = st.checkbox("Background Jobs / Schedulers")
        ci_cd_required = st.checkbox("CI/CD Required")

        submit_migrate = st.form_submit_button("Generate Migration Options")

    # ---------------------------
    # BUILD PAYLOAD
    # ---------------------------
    if submit_migrate:
        mig_payload = {
            "application_profile": {
                "name": app_name,
                "size": application_size,
                "type": application_type,
                "statefulness": statefulness
            },
            "technology_stack": {
                "frontend": frontend_tech,
                "backend": backend_tech,
                "middleware": middleware_used,
                "database": database_engine
            },
            "compute": {
                "hosting_preference": hosting_preference,
                "os_type": os_type,
                "containerized": containerized
            },
            "data": {
                "data_size_gb": data_size_gb,
                "backup_required": backup_required
            },
            "security": {
                "auth_method": auth_method,
                "compliance": compliance
            },
            "connectivity": {
                "end_user_client": end_user_client,
                "network_port": network_port,
                "external_dependency": external_dependency
            },
            "operations": {
                "background_jobs": background_jobs,
                "ci_cd_required": ci_cd_required
            }
        }

        st.session_state.mig_payload = mig_payload

        with st.spinner("Generating migration options using GPT-5.2..."):
            try:
                st.session_state.mig_suggestions = new_application(
                    mig_payload,
                    mode="migrate"
                )
            except Exception as e:
                st.error(f"GPT call failed: {e}")
                st.stop()

        store_gpt_output(mig_payload, st.session_state.mig_suggestions)

    # ---------------------------
    # SHOW MIGRATION OPTIONS
    # ---------------------------
    if st.session_state.mig_suggestions:
        st.subheader("Migration Architecture Options")

        titles = [
            opt.get("title", f"Option {i+1}")
            for i, opt in enumerate(st.session_state.mig_suggestions)
        ]

        choice = st.radio("Choose a migration option", titles)

        selected = st.session_state.mig_suggestions[titles.index(choice)]
        st.session_state.selected_migration_option = selected

        st.json(selected)
