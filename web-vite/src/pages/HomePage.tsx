import { ContactStrip } from '../components/sections/ContactStrip'
import { ExpertiseStrip } from '../components/sections/ExpertiseStrip'
import { FeaturedProjectsSection } from '../components/sections/FeaturedProjectsSection'
import { HeroSection } from '../components/sections/HeroSection'

export default function HomePage() {
  return (
    <>
      <HeroSection />
      <ExpertiseStrip />
      <FeaturedProjectsSection />
      <ContactStrip />
    </>
  )
}
