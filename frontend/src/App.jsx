import { useEffect, useState } from 'react'
import { fetchHealth } from './api'
import StatusCard from './components/StatusCard'

export default function App() {
  const [status, setStatus] = useState('loading')

  useEffect(() => {
    fetchHealth()
      .then((data) => setStatus(data.status ?? 'unknown'))
      .catch(() => setStatus('offline'))
  }, [])

  return (
    <main className="app-shell">
      <h1>DDFEM</h1>
      <StatusCard status={status} />
    </main>
  )
}
