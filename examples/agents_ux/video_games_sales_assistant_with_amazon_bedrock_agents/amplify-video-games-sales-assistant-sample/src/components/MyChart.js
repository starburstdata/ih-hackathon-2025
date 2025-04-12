import React, { useState, useEffect } from "react";
import Chart from "react-apexcharts";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import Alert from "@mui/material/Alert";

const MyChart = ({ caption, options, series, type }) => {
  const [chartOptions, setChartOptions] = useState(options);
  const [chartSeries, setChartSeries] = useState(series);

  useEffect(() => {
    console.log("Apply chart configuration modifications to: ", options);

    const updatedOptions = { ...options };
    
    // Disable zoom functionality
    if (!updatedOptions.chart) {
      updatedOptions.chart = {};
    }
    if (!updatedOptions.chart.zoom) {
      updatedOptions.chart.zoom = {};
    }
    updatedOptions.chart.zoom.enabled = false;
    
    // Center align title if it exists
    if (updatedOptions.hasOwnProperty("title")) {
      updatedOptions.title.align = "center";
    }
    
    // Center align subtitle if it exists
    if (updatedOptions.hasOwnProperty("subtitle")) {
      updatedOptions.subtitle.align = "center";
    }
    console.log("Chart configuration: ", updatedOptions);
    setChartOptions(updatedOptions);
  }, [options]);

  return (
    <Box>
      <Typography component="div" variant="body1">
        <ReactMarkdown remarkPlugins={[[remarkGfm, { singleTilde: false }]]}>
          {caption}
        </ReactMarkdown>
      </Typography>
      <Box
        sx={(theme) => ({
          pt: 1,
          pb: 2,
          pl: 2,
          pr: 2,
          m: 0,
          mb: 1,
          borderRadius: 4,
          boxShadow: "rgba(0, 0, 0, 0.05) 0px 4px 12px",
        })}
      >
        {/* Error boundary for the Chart component */}
        <ErrorBoundary
          fallback={
            <Alert severity="error">
              Failed to render chart. Please check your chart configuration.
            </Alert>
          }
        >
          <Chart
            options={chartOptions}
            series={chartSeries}
            type={type}
            height={420}
          />
        </ErrorBoundary>
      </Box>
    </Box>
  );
};

// Error Boundary component to catch render errors
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error("Chart error:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback;
    }
    return this.props.children;
  }
}

export default MyChart;