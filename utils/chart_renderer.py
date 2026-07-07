import streamlit as st
import plotly.express as px
import uuid


class ChartRenderer:

    def render(self, dataframe, visualization):
        """
        Render charts based on visualization recommendation.
        """

        try:

            chart_type = (
                visualization.get("chart_type", "")
                .strip()
                .lower()
                .replace(" ", "_")
            )
            x_axis = visualization.get("x_axis")
            y_axis = visualization.get("y_axis")
            title = visualization.get("title", "Chart")

            # ---------------------------------
            # Validate dataframe columns
            # ---------------------------------

            if x_axis not in dataframe.columns:
                st.error(f"❌ X-axis column '{x_axis}' not found.")
                return

            if y_axis not in dataframe.columns:
                st.error(f"❌ Y-axis column '{y_axis}' not found.")
                return

            # ---------------------------------
            # BAR CHART
            # ---------------------------------

            if chart_type in ["bar", "bar_chart"]:

                fig = px.bar(
                    dataframe,
                    x=x_axis,
                    y=y_axis,
                    title=title,
                    text_auto=".2s"
                )

                fig.update_layout(
                    height=450,
                    title_x=0.5,
                    xaxis_title=x_axis.replace("_", " ").title(),
                    yaxis_title=y_axis.replace("_", " ").title(),
                    xaxis=dict(categoryorder="total descending")
                )

                fig.update_traces(
                    textposition="outside"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True,
                    key=f"chart_{uuid.uuid4()}",
                    config={
                        "displaylogo": False,
                        "modeBarButtonsToRemove": [
                            "lasso2d",
                            "select2d"
                        ]
                    }
                )

            # ---------------------------------
            # LINE CHART
            # ---------------------------------

            elif chart_type in ["line", "line_chart"]:

                fig = px.line(
                    dataframe,
                    x=x_axis,
                    y=y_axis,
                    title=title,
                    markers=True
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True,
                    key=f"chart_{uuid.uuid4()}"
                )

            # ---------------------------------
            # PIE CHART
            # ---------------------------------

            elif chart_type in ["pie", "pie_chart"]:

                fig = px.pie(
                    dataframe,
                    names=x_axis,
                    values=y_axis,
                    title=title
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True,
                    key=f"chart_{uuid.uuid4()}"
                )

            # ---------------------------------
            # SCATTER CHART
            # ---------------------------------

            elif chart_type in ["scatter", "scatter_plot"]:

                fig = px.scatter(
                    dataframe,
                    x=x_axis,
                    y=y_axis,
                    title=title
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True,
                    key=f"chart_{uuid.uuid4()}"
                )

            else:
                st.warning(f"Unsupported chart type: {chart_type}")

        except Exception as e:

            st.error("❌ Chart Rendering Failed")
            st.exception(e)