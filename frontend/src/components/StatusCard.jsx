export default function StatusCard({ status }) {
  return (
    <section className="status-card">
      <h2>Backend Health</h2>
      <p>Current status: {status}</p>
    </section>
  )
}
