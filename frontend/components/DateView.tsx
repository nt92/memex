import React, { useState } from 'react'
import { parseDate } from '../utils/utils'
import { useSupabaseClient, useUser } from '@supabase/auth-helpers-react'
import { Database } from '../utils/database.types'
import { Timeline, TimelineEvent } from './timeline'
type Record = Database['public']['Tables']['records']['Row']

const DateView = () => {
  const supabase = useSupabaseClient<Database>()
  const user = useUser()
  const [date, setDate] = useState('')
  const [records, setRecords] = useState<Record[]>([])

  async function getRecordsByDates() {
    try {
      if (!user) throw new Error('No user')

      const dateObj = new Date(date + ' 00:00:00')
      const tzOffst = dateObj.getTimezoneOffset() * 60000
      const startDate = new Date(dateObj.getTime() + tzOffst).toISOString()
      const endDate = new Date(
        dateObj.getTime() + tzOffst + 86400000
      ).toISOString()

      const { data, error, status } = await supabase
        .from('records')
        .select(`id, source, title, content, time, link`)
        .gte('time', startDate)
        .lte('time', endDate)
        .order('time', { ascending: false })

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
    }
  }

  return (
    <div>
      <div className="flex items-center">
        <input
          type="date"
          className="py-2 px-3 rounded-md placeholder-gray-500 text-gray-700 leading-tight focus:outline-none focus:shadow-outline-blue focus:border-blue-300 bg-gray-100"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />
        <button
          type="button"
          className="mx-3 py-2 px-3 rounded-md text-sm font-medium leading-5 text-gray-700 hover:text-gray-500 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 active:bg-gray-50 active:text-gray-800 bg-gray-100"
          onClick={getRecordsByDates}
        >
          Search
        </button>
      </div>
      <Timeline>
        {records.map((record) => (
          <TimelineEvent
            key={record.id}
            title={record.title}
            createdAt={parseDate(record.time)}
            icon={<i className="material-icons md-18">{record.source}</i>}
          >
            {record.content}
          </TimelineEvent>
        ))}
      </Timeline>
    </div>
  )
}

export default DateView
