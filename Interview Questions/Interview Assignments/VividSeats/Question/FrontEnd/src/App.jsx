import { useEffect } from "react";
import "./App.css";
import { useState } from "react";

function App() {
  const [response, setResponse] = useState([]);
  const [csvData, setCsvData] = useState([]);

  async function fetchCSV() {
    const data = await fetch(`${import.meta.env.VITE_BACKEND}/v1/csv`);
    const json = await data.json();
    setCsvData(json);
  }

  useEffect(() => {
    function fetchLog() {
      fetch(`${import.meta.env.VITE_BACKEND}/v1/log`)
        .then((data) => data.json())
        .then((json) => setResponse(json))
        .catch((err) => console.log(err));
    }

    fetchLog();
  }, []);

  return (
    <>
      <>
        <p>CSV Data</p>
        <button className="button" onClick={fetchCSV}>
          Get CSV
        </button>
        <p>{JSON.stringify(csvData)}</p>
      </>
      <>
        <p>Log Data</p>
        <p>{JSON.stringify(response)}</p>
      </>
    </>
  );
}

export default App;
