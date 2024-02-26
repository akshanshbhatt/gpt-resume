import ResumeUpload from "@/components/resume-upload"
import { NavBar } from "@/components/nav-bar";

export default function Home() {
  return (
    <div style={{ paddingTop: '100px' }}>
      <NavBar />
      <div>
        <ResumeUpload />
      </div>
    </div>
  )
}
