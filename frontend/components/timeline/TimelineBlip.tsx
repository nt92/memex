import React from 'react'
import s from './styles'

type TimelineBlipProps = {
  title: React.ReactNode
  icon?: React.ReactNode
  iconColor?: string
  iconStyle?: React.CSSProperties
  orientation?: string
  style?: React.CSSProperties
}

function TimelineBlip(props: TimelineBlipProps) {
  const {
    title,
    icon,
    iconColor,
    iconStyle = {},
    orientation,
    style = {},
    ...otherProps
  } = props

  function mergeNotificationStyle(
    iconColor: string | undefined
  ): React.CSSProperties {
    return iconColor
      ? {
          ...(s.eventType as React.CSSProperties),
          ...{ color: iconColor, borderColor: iconColor },
        }
      : (s.eventType as React.CSSProperties)
  }

  function getIconStyle(iconStyle: React.CSSProperties): React.CSSProperties {
    return { ...(s.materialIcons as React.CSSProperties), ...iconStyle }
  }

  const leftOrRightEvent: React.CSSProperties =
    orientation === 'right'
      ? { ...(s['event--right'] as React.CSSProperties) }
      : { ...(s['event--left'] as React.CSSProperties) }
  return (
    <div
      style={{
        ...(s.event as React.CSSProperties),
        marginBottom: 50,
        ...style,
      }}
    >
      <div style={mergeNotificationStyle(iconColor)}>
        <span style={getIconStyle(iconStyle)}>{icon}</span>
      </div>
      <div
        {...otherProps}
        style={{ ...(s.blipStyle as React.CSSProperties), ...leftOrRightEvent }}
      >
        <div>{title}</div>
      </div>
      <div style={s.eventAfter as React.CSSProperties} />
    </div>
  )
}

export default TimelineBlip
