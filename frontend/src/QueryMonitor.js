import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement);

/**
 * A React component that fetches query logs from a Flask API endpoint and renders
 * them as a bar chart using Chart.js. The chart shows the number of queries
 * over time, with each bar representing a single query.
 *
 * @returns {React.ReactElement} The React component to render.
 */
function QueryMonitor() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetch('http://your-gcp-url/monitor')
      .then(res => res.json())
      .then(data => setLogs(data.logs));
  }, []);

  const chartData = {
    labels: logs.map(log => log.timestamp),
    datasets: [{ label: 'Queries', data: logs.map(log => 1), backgroundColor: 'blue' }],
  };

  return (
    <div>
      <h2>Query Logs</h2>
      <Bar data={chartData} />
    </div>
  );
}
export default QueryMonitor;