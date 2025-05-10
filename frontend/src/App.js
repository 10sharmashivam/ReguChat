import React, { useEffect, useState } from 'react';
import QueryMonitor from './QueryMonitor';

/**
 * The main entry point for the React application.
 *
 * This component renders a QueryMonitor component inside a div.
 *
 * @returns {React.ReactElement} The React component to render.
 */
function App() {
  return (
    <div>
      <h1>ReguChat Dashboard</h1>
      <QueryMonitor />
    </div>
  );
}
export default App;