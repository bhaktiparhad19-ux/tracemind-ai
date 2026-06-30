import streamlit as st
from modules.log_parser import AuthenticationLogParser
from modules.threat_detector import ThreatDetector
from modules.ai_analyst import AIAnalyst

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="TraceMind AI",
    page_icon="🛡️",
    layout="wide"
)

# -------------------------------------------------
# Header
# -------------------------------------------------

st.title("🛡️ TraceMind AI")
st.subheader("AI-Powered Digital Forensics & Incident Response Platform")

st.markdown(
"""
Upload a Linux authentication log and let TraceMind AI:

- 🔍 Parse authentication events
- 🚨 Detect cyber attacks
- 🎯 Extract Indicators of Compromise (IOCs)
- 🤖 Generate an AI-powered DFIR Incident Report
"""
)

st.divider()

# -------------------------------------------------
# Upload
# -------------------------------------------------

uploaded_file = st.file_uploader(
    "📂 Upload Authentication Log",
    type=["log", "txt"]
)

# -------------------------------------------------
# Main Analysis
# -------------------------------------------------

if uploaded_file:

    st.success("✅ Log uploaded successfully!")

    if st.button("🚀 Analyze Log", use_container_width=True):

        with st.spinner("Analyzing authentication logs..."):

            logs = uploaded_file.read().decode("utf-8")

            events = AuthenticationLogParser(logs).parse()

            threat = ThreatDetector(events).analyze()

            report = AIAnalyst(threat).analyze()

        st.success("✅ Analysis Completed Successfully!")

        st.balloons()

        st.divider()

        # ----------------------------------------
        # Threat Summary
        # ----------------------------------------

        st.header("📊 Threat Summary")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Attack Type",
            threat["attack_type"]
        )

        col2.metric(
            "Severity",
            threat["severity"]
        )

        col3.metric(
            "Confidence",
            f'{threat["confidence"]}%'
        )

        st.divider()

        # ----------------------------------------
        # Attack Chain
        # ----------------------------------------

        st.header("⚔️ Attack Chain")

        if threat["attack_chain"]:

            for step in threat["attack_chain"]:
                st.success(step)

        else:
            st.info("No attack chain detected.")

        st.divider()

        # ----------------------------------------
        # Indicators of Compromise
        # ----------------------------------------

        st.header("🎯 Indicators of Compromise")

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("🌐 Suspicious IP Addresses")

            if threat["ioc"]["suspicious_ips"]:

                for ip in threat["ioc"]["suspicious_ips"]:
                    st.code(ip)

            else:
                st.info("None")

        with col2:

            st.subheader("👤 Target Users")

            if threat["ioc"]["target_users"]:

                for user in threat["ioc"]["target_users"]:
                    st.code(user)

            else:
                st.info("None")

        st.divider()

        # ----------------------------------------
        # AI Report
        # ----------------------------------------

        st.header("🤖 AI Incident Report")

        st.markdown(report)

        st.download_button(
            label="📥 Download Incident Report",
            data=report,
            file_name="incident_report.md",
            mime="text/markdown",
            use_container_width=True
        )

        st.divider()

        # ----------------------------------------
        # Expanders
        # ----------------------------------------

        with st.expander("📋 Parsed Security Events"):

            st.write(events)

        with st.expander("📄 Uploaded Log File"):

            st.code(logs)

# -------------------------------------------------
# Footer
# -------------------------------------------------

st.divider()

st.caption(
    "TraceMind AI • AI-Powered Digital Forensics & Incident Response Platform"
)