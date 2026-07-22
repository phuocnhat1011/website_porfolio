interface ProjectPageHeaderProps {
  title: string
  description: string
}

export function ProjectPageHeader({ title, description }: ProjectPageHeaderProps) {
  return (
    <header className="pageHeader">
      <h1>{title}</h1>
      <p className="pageIntro">{description}</p>
    </header>
  )
}
