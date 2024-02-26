"use client";
import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import PDFUpload from "@/components/pdf-upload";
import { useDropzone } from "react-dropzone";
import AddJob from "./job-dialog";
import axios from 'axios';
// import { useRouter } from "next/navigation";

const ResumeUpload = () => {
  const [files, setFiles] = useState<File[]>([]);
  const { acceptedFiles, getRootProps, getInputProps } = useDropzone({
    accept: {
      "application/pdf": [".pdf"],
    },
    multiple: true,
    onDrop: (acceptedFiles: File[]) => {
      setFiles(acceptedFiles);
    }
  });

  const handleDialogSubmit = (jobTitle: string | Blob, jobDescription: string | Blob) => {
    console.log(jobTitle, jobDescription);
    const formData = new FormData();
    formData.append("job_title", jobTitle);
    formData.append("job_description", jobDescription);
    files.forEach((file) => {
      formData.append("files", file);
    });

    axios.post('http://127.0.0.1:8000/api/post-resume-with-job/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        // "Access-Control-Allow-Origin": "*",
        // "Access-Control-Allow-Methods": "POST, PUT, OPTIONS",
        // "Access-Control-Allow-Headers": "Content-Type",
        // "Access-Control-Max-Age": "300"
      }
    }).then(response => {
      console.log(response);
      window.location.href = `/result/${response.data.job_u_id}`;
    }).catch(error => {
      console.error(error);
      // window.location.href = '/result';
    });
  };

  return (
    <>
      <div {...getRootProps({ className: "dropzone" })}>
        <div className="mx-auto border-[#5F5ADB] m-5 w-[40%] p-5 rounded-lg border-[2px] flex flex-col items-center justify-around gap-3">
          {<svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g opacity="0.7">
              <path d="M26.6666 26.6667L19.9999 20L13.3333 26.6667" stroke="#121212" strokeWidth="3.33333" strokeLinecap="round" strokeLinejoin="round" />
              <path d="M20 20V35" stroke="#121212" strokeWidth="3.33333" strokeLinecap="round" strokeLinejoin="round" />
              <path d="M33.9833 30.65C35.6088 29.7638 36.893 28.3615 37.6331 26.6644C38.3731 24.9673 38.527 23.072 38.0703 21.2778C37.6136 19.4836 36.5724 17.8925 35.1111 16.7557C33.6497 15.619 31.8514 15.0012 29.9999 15H27.8999C27.3955 13.0487 26.4552 11.2372 25.1498 9.70165C23.8445 8.16608 22.208 6.94641 20.3634 6.13434C18.5189 5.32227 16.5142 4.93892 14.5001 5.01313C12.4861 5.08734 10.515 5.61716 8.73523 6.56277C6.95541 7.50838 5.41312 8.84516 4.2243 10.4726C3.03549 12.1001 2.23108 13.9759 1.87157 15.959C1.51205 17.9421 1.60678 19.9809 2.14862 21.9221C2.69047 23.8633 3.66534 25.6564 4.99993 27.1667" stroke="#121212" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" />
              <path d="M26.6666 26.6667L19.9999 20L13.3333 26.6667" stroke="#121212" strokeWidth="3.33333" strokeLinecap="round" strokeLinejoin="round" />
            </g>
          </svg>
          }
          <div className="flex w-3/5 justify-around">
            <div className="font-semibold text-sm">
              <span className="font-semibold text-[#5F5ADB]">
                Click to upload PDF
              </span>{" "}
              <span className="font-light">or drag and drop</span>
            </div>
          </div>
        </div>
      </div>

      <div className="mx-auto m-5 w-[40%]">
        {acceptedFiles ? (
          acceptedFiles.map((file) => (
            <PDFUpload
              isUploaded={true}
              fileName={file.name}
              fileSize={(file.size / 1000)}
            />
          ))
        ) : (
          <></>
        )}
      </div>

      <div className="mx-auto m-5 w-1/5 flex items-center justify-around">
        <Button variant="outline" className="w-36">Cancel</Button>
        {/* <Button className="w-36 bg-[#423DDB] hover:bg-[#5F5ADB]">Attach Files</Button> */}
        <AddJob onSubmit={handleDialogSubmit}></AddJob>
      </div>
    </>
  );
};

export default ResumeUpload;
