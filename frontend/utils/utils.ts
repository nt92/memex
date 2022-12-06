const parseDate = (date: string): string => {
  let dateItem = new Date(Date.parse(date))
  return dateItem.toLocaleDateString() + ' ' + dateItem.toLocaleTimeString()
}

export { parseDate }
