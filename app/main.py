import sys
from pathlib import Path


project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

import streamlit as st
import pandas as pd

from services.gemini_service import GeminiService
from agents.intent_agent import IntentAgent
from agents.schema_agent import SchemaAgent
from agents.sql_generator_agent import SQLGeneratorAgent
from agents.sql_validator_agent import SQLValidatorAgent
from agents.execution_agent import ExecutionAgent
from agents.insight_agent import InsightAgent
from agents.visualization_agent import VisualizationAgent
from utils.chart_renderer import ChartRenderer

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="BI Navigator",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("📊 BI Navigator")

st.subheader("Your Agentic Business Intelligence Assistant")

st.markdown("---")

# -----------------------------
# Welcome Message
# -----------------------------
st.write("""
Welcome to **BI Navigator**!

Ask business questions in natural language and let AI agents:
- 🧠 Understand your intent
- 🗂️ Discover the database schema
- 💻 Generate SQL
- ✅ Validate SQL
- 📈 Execute queries
- 💡 Generate business insights
- 📊 Recommend visualizations
""")

st.markdown("---")

# -----------------------------
# User Input
# -----------------------------
question = st.text_input(
    "💬 Ask your business question:",
    placeholder="Example: Show top 5 products by revenue last quarter"
)

# -----------------------------
# Ask Button
# -----------------------------
if st.button("🚀 Ask BI Navigator"):

    if question.strip():

        with st.spinner("🤖 BI Navigator is thinking..."):

            try:

                intent_agent = IntentAgent()

                schema_agent = SchemaAgent()

                sql_agent = SQLGeneratorAgent()

                validator_agent = SQLValidatorAgent()

                execution_agent = ExecutionAgent()

                insight_agent = InsightAgent()

                visualization_agent = VisualizationAgent()

                renderer = ChartRenderer()

                intent = intent_agent.analyze(question)

                schema = schema_agent.discover_schema()

                sql = sql_agent.generate_sql(intent, schema)

                validation = validator_agent.validate_sql(sql)

                st.success("✅ User request successfully interpreted by the Intent Agent.")
                st.subheader("🎯 Analysis Request")

                st.markdown("#### 💬 Business Question")
                st.info(question)

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Analysis Type",
                        intent.get("intent", "N/A").replace("_", " ").title()
                    )

                    st.metric(
                        "Metric",
                        intent.get("metric", "N/A").title()
                    )

                with col2:
                    st.metric(
                        "Dimension",
                        intent.get("dimension", "N/A").title()
                    )

                    confidence = intent.get("confidence", 0)

                    st.metric(
                        "Confidence",
                        f"{confidence:.0%}"
                    )

                time_period = intent.get("time_period")

                if time_period:
                    st.write(f"**Time Period:** {time_period}")
                else:
                    st.write("**Time Period:** Not Specified")

                st.subheader("🗂 Database Schema")

                st.caption("Available tables used by BI Navigator")

                st.success(f"✅ {len(schema)} tables discovered")

                for table_name, columns in schema.items():

                    with st.expander(
                        f"📋 {table_name} ({len(columns)} columns)",
                        expanded=False,
                    ):

                        st.write("**Columns:**")

                        for column in columns:
                            st.markdown(f"- `{column}`")

                st.subheader("💻 Generated SQL")

                st.code(sql, language="sql")

                st.subheader("✅ SQL Validation")

                st.json(validation)

                if validation["valid"]:

                    result = execution_agent.execute(sql)

                    if result["success"]:
                        insights = insight_agent.generate_insights(
                            question,
                            sql,
                            result["rows"]
                        )

                    visualization = visualization_agent.recommend_visualization(
                        question,
                        sql,
                        result["columns"]
                    )

                else:

                    st.error("❌ SQL Validation Failed")

                    st.write(validation["reason"])

                    st.stop()
                
                st.subheader("📊 Query Results")

                if result["success"]:

                    dataframe = pd.DataFrame(result["rows"], columns=result["columns"])

                    st.dataframe(dataframe)

                    st.success(f"{result['row_count']} row(s) returned.")


                    st.subheader("💡 Business Insights")

                    st.markdown("### 📋 Summary")
                    st.write(insights["summary"])

                    st.markdown("### 🔍 Key Findings")

                    for finding in insights["key_findings"]:
                        st.write(f"• {finding}")

                    st.markdown("### 🎯 Recommendations")

                    for recommendation in insights["recommendations"]:
                        st.write(f"• {recommendation}")


                        # -----------------------------------------
                        # Visualization Recommendation
                        # -----------------------------------------

                    st.subheader("📊 Sales Visualization")

                    st.info(
                        visualization.get(
                            "reason",
                            "Recommended visualization based on your business question."
                        )
                    )

                    renderer.render(
                    dataframe,
                    visualization
                    )

                else:

                    st.error(result["error"])


            except Exception as e:

                error_message = str(e)

                if "RESOURCE_EXHAUSTED" in error_message or "429" in error_message:

                    st.error("⚠️ Gemini API quota exceeded.")

                    st.info(
                        "The free Gemini API limit has been reached. "
                        "Please wait for the quota to reset or use another API key."
                    )

                elif "503" in error_message:

                    st.warning("⚠️ Gemini service is temporarily busy.")

                    st.info(
                        "Please wait a few moments and try again."
                    )

                else:

                    st.error(f"Error: {e}")

    else:

        st.warning("Please enter a business question.")

st.markdown("---")

# -----------------------------
# Agent Status
# -----------------------------
st.subheader("🤖 Agent Workflow")

if question.strip():

    st.success("✅ Intent Agent")

    st.success("✅ Schema Agent")

    st.success("✅ SQL Generator Agent")

    st.success("✅ SQL Validator Agent")

    st.success("✅ Execution Agent")

    st.success("✅ Insight Agent")

    st.success("✅ Visualization Agent")