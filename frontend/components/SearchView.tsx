import React, { useState } from 'react'
import { useSupabaseClient, useUser } from '@supabase/auth-helpers-react'
import { Database } from '../utils/database.types'
import { parseDate } from '../utils/utils'
type Record = Database['public']['Tables']['records']['Row']

export default function SearchView() {
  const supabase = useSupabaseClient<Database>()
  const user = useUser()
  const [searchTerm, setSearchTerm] = useState('')
  const [records, setRecords] = useState<Record[]>([])

  async function getRecordsBySearch() {
    try {
      if (!user) throw new Error('No user')

      const { data, error, status } = await supabase
        .from('records')
        .select(`id, source, title, content, time, link`)
        // TODO: eventually figure out a better way to do a FTS instead
        .like('content', '%' + searchTerm + '%')
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
      <div className="relative w-full max-w-md flex items-center">
        <input
          type="text"
          placeholder="Search Term"
          className="w-full py-2 px-3 rounded-md placeholder-gray-500 text-gray-700 leading-tight focus:outline-none focus:shadow-outline-blue focus:border-blue-300 bg-gray-100"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <button
          type="button"
          className="mx-3 py-2 px-3 rounded-md text-sm font-medium leading-5 text-gray-700 hover:text-gray-500 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 active:bg-gray-50 active:text-gray-800 bg-gray-100"
          onClick={getRecordsBySearch}
        >
          Search
        </button>
      </div>
      <ul className="mt-3 list-none">
        {records.map((record) => (
          <div
            key={record.id}
            className="py-2 flex rounded-md hover:bg-gray-100 hover:text-gray-900 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 active:bg-gray-50 active:text-gray-800"
          >
            <li className="py-1 px-3 min-w-[180px] text-xs font-medium text-gray-500">
              {parseDate(record.time)}
            </li>
            <li className="py-0.5 px-3 text-sm font-medium leading-5 text-gray-700">
              {record.title}
              <br />
              {record.content}
            </li>
          </div>
        ))}
      </ul>
    </div>
  )
}

// export default SearchView
