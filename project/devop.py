import streamlit as st
import ollama

st.set_page_config(
    page_title="AI DevOps Log Analyser",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI DevOps Log Analyser")
st.write("✨ Analyse your application logs using AI and Ollama!")

st.divider()

# Log Input

st.header("📋 Log Analysis")

log_text = st.text_area(
    "📝 Enter your log data",
    height=300,
    placeholder="""Example:
ERROR Database connection failed
WARNING Server response time is high
INFO Application started successfully"""
)

st.divider()

# Analysis Options

st.header("⚙️ Analysis Options")

col1, col2 = st.columns(2)

with col1:
    analysis_type = st.selectbox(
        "🔍 Analysis Type",
        [
            "Complete Analysis",
            "Find Errors",
            "Find Warnings",
            "Root Cause Analysis",
            "Suggest Solutions"
        ]
    )

with col2:
    environment = st.selectbox(
        "🌐 Environment",
        [
            "Development",
            "Testing",
            "Production"
        ]
    )

st.divider()

# Analyse Button

if st.button("🚀 Analyse Logs"):

    if log_text == "":
        st.warning("⚠️ Please enter some logs first.")

    else:

        st.success("✅ Log data received!")

        # Log Statistics

        st.header("📊 Log Overview")

        total_lines = len(log_text.splitlines())
        error_count = log_text.upper().count("ERROR")
        warning_count = log_text.upper().count("WARNING")
        info_count = log_text.upper().count("INFO")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "📄 Total Lines",
                total_lines
            )

        with col2:
            st.metric(
                "❌ Errors",
                error_count
            )

        with col3:
            st.metric(
                "⚠️ Warnings",
                warning_count
            )

        with col4:
            st.metric(
                "ℹ️ Info",
                info_count
            )

        st.divider()

        # AI Prompt

        prompt = f"""
You are an expert DevOps engineer and log analysis assistant.

Analyse the following application logs.

Environment:
{environment}

Analysis Type:
{analysis_type}

Logs:
{log_text}

Provide the result in these sections:

1. 🔍 Log Summary
2. ❌ Errors Found
3. ⚠️ Warnings Found
4. 🧠 Possible Root Causes
5. 🛠️ Recommended Solutions
6. 🚀 DevOps Recommendations
7. ✅ Final Action Checklist

Explain the issues clearly and provide practical troubleshooting
steps suitable for a DevOps engineer.
"""

        # Ollama

        try:

            with st.spinner(
                "🤖 Ollama is analysing your logs..."
            ):

                response = ollama.chat(
                    model="llama3.2",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

            result = response["message"]["content"]

            st.success(
                "✨ Log Analysis Completed!"
            )

            st.header("🤖 AI Analysis")

            st.write(result)

            st.divider()

            # Download

            st.download_button(
                "📥 Download Analysis",
                result,
                file_name="AI_DevOps_Log_Analysis.txt",
                mime="text/plain"
            )

        except Exception:

            st.error(
                "❌ Could not connect to Ollama."
            )

            st.info(
                "Please start Ollama using:"
            )

            st.code(
                "ollama run llama3.2"
            )