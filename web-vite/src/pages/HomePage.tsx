import { FeaturedProjectsSection } from '../components/sections/FeaturedProjectsSection'
import { HeroSection } from '../components/sections/HeroSection'
import { ProfileSection } from '../components/sections/ProfileSection'

export default function HomePage() {
  return (
    <>
      <HeroSection />
      <ProfileSection />
      <FeaturedProjectsSection />
    </>
  )
}
