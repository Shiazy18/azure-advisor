import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from typing import Dict, List
from azure.identity import get_bearer_token_provider, DefaultAzureCredential
load_dotenv()
import json

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

#subscription_key = os.getenv("AZURE_OPENAI_API_KEY")
api_version = "2024-12-01-preview"

token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default")


def new_application(payload):
    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=endpoint,
        azure_ad_token_provider=token_provider
    )

    payload_json = json.dumps(payload, indent=2)


    SYSTEM_PROMPT = (
        "You are an Azure Cloud Architecture, Platform, and Cost Optimization Expert."
        "Your task is to analyze application onboarding metadata and produce MULTIPLE"
        "architecture options for Azure onboarding."

        "Rules:"
        "- Generate exactly 3 distinct architecture options"
        "- Each option must have a short, descriptive TITLE"
        "- Each option must represent a different trade-off (cost, scalability, control)"
        "- Decide PaaS, IaaS, or Hybrid per option"
        "- Estimate monthly cost per option"
        "- Respect the provided budget and flag over-budget options"
        "- Prefer PaaS where possible, but include IaaS if justified"
        "- Use modern, supported Azure services only"
        "- Output must be STRICT JSON only"
    )

    user_desc = (
        "Analyze the following application onboarding data and propose exactly 3 Azure"
        "architecture options."
        "Each option must:"
        "1. Have a short, descriptive TITLE"
        "2. Clearly state the deployment model (PaaS / IaaS / Hybrid)"
        "3. List recommended Azure services"
        "4. Provide an estimated monthly cost"
        "5. Indicate whether it fits within the provided budget"
        "6. Include a short rationale"

        "Application Onboarding Data:"
        f"{payload_json}"

    )

    # user_desc = (
    #     f"New app: {payload['app_metadata.name']} "
    #     f"Description: {payload['app_metadata.description']}"
    #     f"type={payload['app_metadata.app_type']} "
    #     f"arch={payload['workload.architecture']} "
    #     f"cost={payload.get("cost.monthly_budget_usd")}"

    # )
    prompt = (
        f"{user_desc}\n\n"
        "Return ONLY a valid JSON array with EXACTLY 3 objects. No code fences, no prose.\n"
        "Each object MUST have:\n"
        "- title (string)\n"
        "- Brief about the application"
        "- deployment_model\n"
        "- confidence\n"
        "- services containing compute, data, integration\n"
        "- networking\n"
        "- cost estimate\n"
        "- tech stack"
        "- rationale (string)\n"
        "- recommendedServices (array)\n"
        "- notes (string)"
    )

    # prompt = (
    #     f"{user_desc}\n\n"
    #     "Return ONLY a valid JSON array with EXACTLY 3 objects. No code fences, no prose.\n"
    #     "Each object MUST have:\n"
    #     '{ "applicationName": string, "title": string, "rationale": string, '
    #     '"recommendedServices": [string,...], "notes": string }'
    # )

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            model=deployment,
            max_completion_tokens=16384,
        )

        text = response.choices[0].message.content
        data = json.loads(text)
        assert isinstance(data, list) and len(data) == 3, "Expected JSON array of exactly 3 objects."
        return data

    finally:
        client.close()


def migrate_application(payload):
    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=endpoint,
        azure_ad_token_provider=token_provider,
    )

    payload_json = json.dumps(payload, indent=2)


    SYSTEM_PROMPT = (
        "You are a senior Azure Cloud Architect and Migration Specialist."

        "Your role is to analyze application inventory metadata and generate:"
        "- Azure target architecture recommendations"
        "- Required Azure resources"
        "- Security, networking, and compliance considerations"
        "- A migration strategy aligned with Azure Cloud Adoption Framework (CAF)"
        "- A budget-aware deployment approach"

        "You MUST:"
       " - Recommend Azure-native services where possible"
        "- Prefer PaaS over IaaS unless constraints exist"
        "- Clearly explain why each Azure resource is required"
        "- Output ONLY valid JSON that conforms strictly to the provided schema"
        "- Avoid generic advice and be specific to the provided inputs"

        "Assume the target cloud is Microsoft Azure."
    )

    user_desc = (
        "Analyze the following application inventory details and generate a complete Azure migration plan."
        "Each option must:"
        "1. Have a short, descriptive TITLE"
        "2. Clearly state the deployment model (PaaS / IaaS / Hybrid)"
        "3. Identify all Azure resources that need to be created."
        "4. Provide architecture recommendations with justification."
        "5. Include security, networking, identity, and monitoring considerations."
        "6. Propose a budget-conscious approach (Dev/Test vs Prod)."
        "7. Highlight migration risks and dependencies."
        "8. Suggest post-migration optimization steps."

        "Application inventory:"
        f"{payload_json}"

    )
    prompt = (
        f"{user_desc}\n\n"
        "Return ONLY a valid JSON array with EXACTLY 3 objects. No code fences, no prose.\n"
        "Each object MUST have:\n"
        "- title (string)\n"
        "- Brief about the application"
        "- deployment_model\n"
        "- confidence\n"
        "- architecture recommendations with justification"
        "- services containing compute, data, integration\n"
        "- networking\n"
        "- cost estimate\n"
        "- tech stack"
        "- recommendedServices (array)\n"
        "- notes (string)"
    )

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            model=deployment,
            max_completion_tokens=16384,
        )

        text = response.choices[0].message.content
        data = json.loads(text)
        assert isinstance(data, list) and len(data) == 3, "Expected JSON array of exactly 3 objects."
        return data

    finally:
        client.close()

# app_name="Test2"
# app_type="Ecom"
# arch="Microservices"
# backend="ASP.net"
# frontend="Angular"
# runtime=".Net"

# payload = {
#             "appName": app_name,
#             "appType": app_type,
#             "architecture": arch,
#             "techStack": {
#                 "backend": backend,
#                 "frontend": frontend,
#                 "runtime": runtime,
#             }
# }

# print(json.dumps(new_application(payload), indent=2))
# input()
