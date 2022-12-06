import { useState, useEffect } from 'react'
import { Session } from '@supabase/auth-helpers-react'
import DateView from "./DateView";
import SearchView from "./SearchView";

export default function Dashboard({ session }: { session: Session }) {
  const [isSearch, setIsSearch] = useState(true)

  useEffect(() => {
    // Load initial data (if any)
  }, [session])

  return (
    <div className="w-full max-w-md mx-auto">
      <button
        type="button"
        onClick={() => setIsSearch(!isSearch)}
        className="py-2 px-3 my-2 rounded-md text-sm font-medium leading-5 text-gray-700 hover:text-gray-500 focus:outline-none focus:shadow-outline-blue focus:border-blue-300 active:bg-gray-50 bg-gray-100 active:text-gray-800"
      >
        {isSearch ? 'Switch to Date' : 'Switch to Search'}
      </button>
      <div className="">
        {isSearch ? <SearchView /> : <DateView />}
      </div>
    </div>
  )
}
