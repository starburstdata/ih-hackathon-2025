import React, { useState, useEffect } from "react";
import Chart from "react-apexcharts";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import Alert from "@mui/material/Alert";

const MyChart = ({ caption, options, series, type }) => {
  const [error, setError] = useState(null);
  const [chartOptions, setChartOptions] = useState(options);
  const [chartSeries, setChartSeries] = useState(series);

  useEffect(() => {
    // Fix for the "Multiple Y Axis for bars" error
    if (type === 'bar' && options?.yaxis?.length > 1) {
      setError("Multiple Y Axis for bars are not supported. Using a single Y axis.");
      // Create a modified options object with a single Y axis
      const modifiedOptions = {
        ...options,
        yaxis: Array.isArray(options.yaxis) ? [options.yaxis[0]] : options.yaxis,
        plotOptions: {
          ...options.plotOptions,
          bar: {
            ...options.plotOptions?.bar,
            horizontal: false
          }
        }
      };
      setChartOptions(modifiedOptions);
    } else {
      setChartOptions(options);
      setError(null);
    }
    
    setChartSeries(series);
  }, [options, series, type]);

  return (
    <Box>
      <Typography component="div" variant="body1">
        <ReactMarkdown remarkPlugins={[[remarkGfm, { singleTilde: false }]]}>
          {caption}
        </ReactMarkdown>
      </Typography>
      <Box
        sx={(theme) => ({
          background: "#FFF",
          pt: 1,
          pb: 2,
          pl: 2,
          pr: 2,
          m: 0,
          mb: 1,
          borderRadius: 4,
          boxShadow: "rgba(0, 0, 0, 0.05) 0px 4px 12px"
        })}
      >
        {error && (
          <Alert severity="warning" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}
        
        {/* Error boundary for the Chart component */}
        <ErrorBoundary fallback={<Alert severity="error">Failed to render chart. Please check your chart configuration.</Alert>}>
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
}

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