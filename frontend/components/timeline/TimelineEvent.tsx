import React, { useState } from 'react'
import s from './styles'

type TimelineEventProps = {
  title: React.ReactNode
  subtitle?: React.ReactNode
  createdAt?: React.ReactNode
  children?: React.ReactNode
  buttons?: React.ReactNode
  container?: string
  icon?: React.ReactNode
  iconColor?: string
  orientation?: string
  collapsible?: boolean
  showContent?: boolean
  className?: string
  onClick?: (evt: React.MouseEvent<HTMLDivElement>) => void
  onIconClick?: (evt: React.MouseEvent<HTMLDivElement>) => void
}

function TimelineEvent(props: TimelineEventProps) {
  const {
    createdAt = undefined,
    title,
    subtitle,
    buttons,
    icon,
    iconColor,
    orientation = 'left',
    showContent = false,
    className = '',
    collapsible,
    onClick,
    onIconClick,
    container,
    children,
  } = props
  const [showContentState, setShowContentState] = useState(showContent)

  function mergeNotificationStyle(
    iconColor: string | undefined,
    orientation: string | undefined
  ): React.CSSProperties {
    const iconColorStyle: React.CSSProperties = iconColor
      ? {
          ...(s.eventType as React.CSSProperties),
          ...{ color: iconColor, borderColor: iconColor },
        }
      : (s.eventType as React.CSSProperties)
    const leftOrRight: React.CSSProperties =
      orientation === 'right'
        ? { ...s['eventType--right'] }
        : { ...s['eventType--left'] }
    return { ...iconColorStyle, ...leftOrRight }
  }

  function mergeContentStyle() {
    return showAsCard() ? s.cardBody : s.message
  }

  function timeStyle(): React.CSSProperties {
    return showAsCard() ? s.time : { ...s.time, color: '#303e49' }
  }

  function showAsCard() {
    return container === 'card'
  }

  function containerStyle(): React.CSSProperties {
    const containerStyle: React.CSSProperties = {
      ...(s.eventContainer as React.CSSProperties),
    }
    return showAsCard()
      ? { ...(s.card as React.CSSProperties), ...containerStyle }
      : containerStyle
  }

  function toggleStyle(): React.CSSProperties {
    const messageStyle = container === 'card' ? { ...s.cardTitle } : {}
    return collapsible ? { ...s.toggleEnabled, ...messageStyle } : messageStyle
  }

  function toggleContent() {
    setShowContentState(!showContentState)
  }

  function renderChildren() {
    return (collapsible && showContent) || !collapsible ? (
      <div style={mergeContentStyle()}>
        {children}
        <div style={s.messageAfter as React.CSSProperties} />
      </div>
    ) : (
      <span
        style={{ fontWeight: 500, fontSize: 16, cursor: 'pointer' }}
        onClick={toggleContent}
      >
        …
      </span>
    )
  }

  const leftOrRightEventStyling: React.CSSProperties =
    orientation === 'right'
      ? { ...(s['event--right'] as React.CSSProperties) }
      : { ...(s['event--left'] as React.CSSProperties) }
  const leftOrRightButtonStyling: React.CSSProperties =
    orientation === 'left'
      ? { ...(s['actionButtons--right'] as React.CSSProperties) }
      : { ...(s['actionButtons--left'] as React.CSSProperties) }
  return (
    <div
      style={{
        ...(s.event as React.CSSProperties),
        ...leftOrRightEventStyling,
      }}
    >
      <div style={mergeNotificationStyle(iconColor, orientation)}>
        <span
          style={{ ...(s.materialIcons as React.CSSProperties) }}
          onClick={onIconClick}
        >
          {icon}
        </span>
      </div>
      <div style={containerStyle()} {...{ onClick, className }}>
        <div style={s.eventContainerBefore} />
        <div
          style={toggleStyle()}
          onClick={collapsible ? toggleContent : undefined}
        >
          {createdAt && <div style={timeStyle()}>{createdAt}</div>}
          <div>{title}</div>
          {subtitle && <div style={{ ...s.subtitle }}>{subtitle}</div>}
          <div style={{ ...s.actionButtons, ...leftOrRightButtonStyling }}>
            {buttons}
          </div>
        </div>
        {children && renderChildren()}
      </div>
      <div style={s.eventAfter as React.CSSProperties} />
    </div>
  )
}

export default TimelineEvent
