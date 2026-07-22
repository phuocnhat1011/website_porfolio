import { Link } from 'react-router-dom'
import { projects } from '../../data/projects'
import type { Project } from '../../types'
import styles from './HomeSections.module.css'

function ProjectCard({ project }: { project: Project }) {
  return (
    <article className={`${styles.projectCard} surface`}>
      <picture className={styles.projectCover}>
        <source srcSet={project.cover} type="image/webp" />
        <img src={project.coverOriginal} alt={`Preview ${project.title}`} loading="lazy" width="1592" height="754" />
      </picture>
      <div className={styles.projectBody}>
        <h3>{project.title}</h3>
        <div className={styles.projectBadges}>
          {project.stack.map((stack) => <span key={stack} className="badge">{stack}</span>)}
        </div>
        <Link className="button buttonPrimary" to={project.route}>Chi tiết dự án</Link>
      </div>
    </article>
  )
}

export function FeaturedProjectsSection() {
  const featuredProjects = projects.filter((project) => project.visibleOnHome)
  return (
    <section className={styles.featured} aria-labelledby="featured-heading">
      <hr />
      <h2 id="featured-heading" className="sectionTitle">Dự án Tiêu Biểu</h2>
      <p className="muted">Các dự án phân tích dữ liệu tài chính — bấm vào “Chi tiết dự án”.</p>
      <div className={styles.projectGrid}>
        {featuredProjects.map((project) => <ProjectCard key={project.id} project={project} />)}
      </div>
    </section>
  )
}
