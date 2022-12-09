import React, { ReactNode } from 'react'
import s from './styles'

type TimelineProps = {
  children: React.ReactNode
  orientation?: string
  style?: React.CSSProperties
  lineColor?: string
  lineStyle?: React.CSSProperties
}

function Timeline(props: TimelineProps) {
  const {
    children,
    orientation = 'left',
    style = {},
    lineColor,
    lineStyle = {},
  } = props
  const childrenWithProps = React.Children.map<ReactNode, ReactNode>(
    children,
    (child) => {
      if (React.isValidElement(child)) {
        return React.cloneElement(child, orientation)
      }
      return child
    }
  )
  const leftOrRight =
    orientation === 'right'
      ? { ...s['containerBefore--right'] }
      : { ...s['containerBefore--left'] }
  let lineAppearance: React.CSSProperties = { ...leftOrRight, ...lineStyle }
  lineAppearance = lineColor
    ? { ...lineAppearance, background: lineColor }
    : lineAppearance
  return (
    <div>
      <section style={{ ...(s.container as React.CSSProperties), ...style }}>
        <div
          style={{
            ...(s.containerBefore as React.CSSProperties),
            ...lineAppearance,
          }}
        />
        {childrenWithProps}
        <div style={s.containerAfter as React.CSSProperties} />
      </section>
    </div>
  )
}

export default Timeline
