import { useState, useEffect } from 'react'
import {useSupabaseClient, Session, useUser} from '@supabase/auth-helpers-react'
import { Database } from '../utils/database.types'
type Record = Database['public']['Tables']['records']['Row']

export default function Dashboard({ session }: { session: Session }) {
  const supabase = useSupabaseClient<Database>()
  const user = useUser()
  const [searchTerm, setSearchTerm] = useState('')
  const [records, setRecords] = useState<Record[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Load initial data (if any)
  }, [session])

  async function getRecordsBySearch() {
    try {
      setLoading(true)
      if (!user) throw new Error('No user')

      let { data, error, status } = await supabase
        .from('records')
        .select(`id, source, title, content, time, link`)
        .textSearch('content', searchTerm)

      if (error && status !== 406) {
        throw error
      }

      if (data) {
        setRecords(data)
      }
    } catch (error) {
      alert('Error loading user data!')
      console.log(error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <div className="searchInput">
        <input type="text" placeholder="Search" value={searchTerm} onChange={(e) => setSearchTerm(e.target.value)} />
      </div>
      <button onClick={getRecordsBySearch}>Search</button>
      <div className="records">
        {records.map((record) => (
          <div key={record.id}>
            <p>[{record.time}] {record.title}: {record.content}</p>
          </div>
        ))}
      </div>
    </div>
  )
}
