import { useId, useRef, useState, type KeyboardEvent, type ReactNode } from 'react'
import styles from './ProjectTabs.module.css'

export interface ProjectTab {
  id: string
  label: string
  content: ReactNode
}

interface ProjectTabsProps {
  tabs: ProjectTab[]
  label: string
}

export function ProjectTabs({ tabs, label }: ProjectTabsProps) {
  const [activeId, setActiveId] = useState(tabs[0]?.id ?? '')
  const prefix = useId().replaceAll(':', '')
  const tabRefs = useRef<Array<HTMLButtonElement | null>>([])

  const activateAt = (index: number) => {
    const tab = tabs[index]
    if (!tab) return
    setActiveId(tab.id)
    tabRefs.current[index]?.focus()
  }

  const handleKeyDown = (event: KeyboardEvent<HTMLButtonElement>, index: number) => {
    let next = index
    if (event.key === 'ArrowRight') next = (index + 1) % tabs.length
    else if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length
    else if (event.key === 'Home') next = 0
    else if (event.key === 'End') next = tabs.length - 1
    else return
    event.preventDefault()
    activateAt(next)
  }

  const activeTab = tabs.find((tab) => tab.id === activeId) ?? tabs[0]

  return (
    <div className={styles.tabs}>
      <div className={styles.tabList} role="tablist" aria-label={label}>
        {tabs.map((tab, index) => {
          const selected = tab.id === activeTab?.id
          return (
            <button
              key={tab.id}
              ref={(element) => { tabRefs.current[index] = element }}
              type="button"
              role="tab"
              id={`${prefix}-tab-${tab.id}`}
              aria-selected={selected}
              aria-controls={`${prefix}-panel-${tab.id}`}
              tabIndex={selected ? 0 : -1}
              onClick={() => setActiveId(tab.id)}
              onKeyDown={(event) => handleKeyDown(event, index)}
            >
              {tab.label}
            </button>
          )
        })}
      </div>
      {activeTab && (
        <div
          className={styles.panel}
          role="tabpanel"
          id={`${prefix}-panel-${activeTab.id}`}
          aria-labelledby={`${prefix}-tab-${activeTab.id}`}
        >
          {activeTab.content}
        </div>
      )}
    </div>
  )
}
