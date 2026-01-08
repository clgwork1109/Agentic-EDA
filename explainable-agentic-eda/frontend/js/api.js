const API_BASE = "http://127.0.0.1:8000/api/v1";

async function uploadDataset(file) {
  const form = new FormData();
  form.append("file", file);

  const res = await fetch(`${API_BASE}/datasets`, {
    method: "POST",
    body: form
  });

  return res.json();
}

async function runEDAJob(datasetId) {
  const res = await fetch(`${API_BASE}/eda/run?dataset_id=${datasetId}`, {
    method: "POST"
  });
  return res.json();
}

async function getResults(jobId) {
  const res = await fetch(`${API_BASE}/eda/results/${jobId}`);
  return res.json();
}
