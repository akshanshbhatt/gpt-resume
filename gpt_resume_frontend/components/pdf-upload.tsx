// import React from "react";

// // import { Check, Loader2 } from "lucide-react";

// interface PDFUploadProps {
//     fileName?: string;
//     fileSize?: number;
//     isUploaded: boolean;
// }

// const PDFUpload: React.FC<PDFUploadProps> = (
//     props: PDFUploadProps
// ) => {
//     return (
//         <div className="w-full border-[.5px] border-gray-300 rounded-lg p-4 flex">
//             <div>
//                 <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
//                     <path d="M4 4C4 1.79086 5.79086 0 8 0H24L36 12V36C36 38.2091 34.2091 40 32 40H8C5.79086 40 4 38.2091 4 36V4Z" fill="#D92D20" />
//                     <path opacity="0.3" d="M24 0L36 12H28C25.7909 12 24 10.2091 24 8V0Z" fill="white" />
//                     <path d="M11.7491 32V25.4545H14.3315C14.8279 25.4545 15.2508 25.5494 15.6003 25.739C15.9497 25.9265 16.216 26.1875 16.3993 26.522C16.5847 26.8544 16.6773 27.2379 16.6773 27.6726C16.6773 28.1072 16.5836 28.4908 16.3961 28.8232C16.2086 29.1555 15.9369 29.4144 15.5811 29.5998C15.2274 29.7852 14.7991 29.8778 14.2963 29.8778H12.6503V28.7688H14.0726C14.3389 28.7688 14.5584 28.723 14.731 28.6314C14.9057 28.5376 15.0356 28.4087 15.1209 28.2447C15.2082 28.0785 15.2519 27.8878 15.2519 27.6726C15.2519 27.4553 15.2082 27.2656 15.1209 27.1037C15.0356 26.9396 14.9057 26.8129 14.731 26.7234C14.5562 26.6317 14.3347 26.5859 14.0662 26.5859H13.1329V32H11.7491ZM19.8965 32H17.5762V25.4545H19.9157C20.5741 25.4545 21.1408 25.5856 21.616 25.8477C22.0911 26.1076 22.4565 26.4815 22.7122 26.9695C22.97 27.4574 23.0989 28.0412 23.0989 28.7209C23.0989 29.4027 22.97 29.9886 22.7122 30.4787C22.4565 30.9687 22.089 31.3448 21.6096 31.6069C21.1323 31.869 20.5613 32 19.8965 32ZM18.9601 30.8143H19.839C20.2481 30.8143 20.5922 30.7418 20.8713 30.5969C21.1526 30.4499 21.3635 30.223 21.5041 29.9162C21.6469 29.6072 21.7183 29.2088 21.7183 28.7209C21.7183 28.2372 21.6469 27.842 21.5041 27.5352C21.3635 27.2283 21.1536 27.0025 20.8745 26.8576C20.5954 26.7127 20.2513 26.6403 19.8422 26.6403H18.9601V30.8143ZM24.1241 32V25.4545H28.4579V26.5955H25.5079V28.1552H28.1702V29.2962H25.5079V32H24.1241Z" fill="white" />
//                 </svg>
//             </div>
//             <div className="text-sm mx-4">
//                 <div className="font-light">Resume.pdf</div>
//                 <div className="font-thin">200KB-100% uploaded</div>
//             </div>
//             <div className="grow flex items-center justify-end">
//                 <div>Test
//                     {/* {props.isUploaded ? (
//             <Check className="bg-[#5F5ADB] text-white rounded-md p-1 font-bold" />
//           ) : (
//             <Loader2 className="text-[#5F5ADB] animate-spin" />
//           )} */
//                     }
//                 </div>
//             </div>
//         </div>
//     );
// };

// export default PDFUpload;



import React from "react";

import { Check, Loader2 } from "lucide-react";

interface PdfUploadProps {
    fileName?: string;
    fileSize?: number;
    isUploaded: boolean;
}

const PdfUpload: React.FC<PdfUploadProps> = (
    props: PdfUploadProps
) => {
    return (
        <div className="w-full border-[.5px] border-gray-300 rounded-lg p-4 flex my-3">
            <div>
                <svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M4 4C4 1.79086 5.79086 0 8 0H24L36 12V36C36 38.2091 34.2091 40 32 40H8C5.79086 40 4 38.2091 4 36V4Z" fill="#D92D20" />
                    <path opacity="0.3" d="M24 0L36 12H28C25.7909 12 24 10.2091 24 8V0Z" fill="white" />
                    <path d="M11.7491 32V25.4545H14.3315C14.8279 25.4545 15.2508 25.5494 15.6003 25.739C15.9497 25.9265 16.216 26.1875 16.3993 26.522C16.5847 26.8544 16.6773 27.2379 16.6773 27.6726C16.6773 28.1072 16.5836 28.4908 16.3961 28.8232C16.2086 29.1555 15.9369 29.4144 15.5811 29.5998C15.2274 29.7852 14.7991 29.8778 14.2963 29.8778H12.6503V28.7688H14.0726C14.3389 28.7688 14.5584 28.723 14.731 28.6314C14.9057 28.5376 15.0356 28.4087 15.1209 28.2447C15.2082 28.0785 15.2519 27.8878 15.2519 27.6726C15.2519 27.4553 15.2082 27.2656 15.1209 27.1037C15.0356 26.9396 14.9057 26.8129 14.731 26.7234C14.5562 26.6317 14.3347 26.5859 14.0662 26.5859H13.1329V32H11.7491ZM19.8965 32H17.5762V25.4545H19.9157C20.5741 25.4545 21.1408 25.5856 21.616 25.8477C22.0911 26.1076 22.4565 26.4815 22.7122 26.9695C22.97 27.4574 23.0989 28.0412 23.0989 28.7209C23.0989 29.4027 22.97 29.9886 22.7122 30.4787C22.4565 30.9687 22.089 31.3448 21.6096 31.6069C21.1323 31.869 20.5613 32 19.8965 32ZM18.9601 30.8143H19.839C20.2481 30.8143 20.5922 30.7418 20.8713 30.5969C21.1526 30.4499 21.3635 30.223 21.5041 29.9162C21.6469 29.6072 21.7183 29.2088 21.7183 28.7209C21.7183 28.2372 21.6469 27.842 21.5041 27.5352C21.3635 27.2283 21.1536 27.0025 20.8745 26.8576C20.5954 26.7127 20.2513 26.6403 19.8422 26.6403H18.9601V30.8143ZM24.1241 32V25.4545H28.4579V26.5955H25.5079V28.1552H28.1702V29.2962H25.5079V32H24.1241Z" fill="white" />
                </svg>
            </div>
            <div className="text-sm mx-4">
                <div>{props.fileName}</div>
                <div className="font-regular">{props.fileSize} KB - 100% Uploaded</div>
            </div>
            <div className="grow flex items-center justify-end">
                <div>
                    {props.isUploaded ? (
                        <Check className="bg-[#5F5ADB] text-white rounded-md p-1 font-bold" />
                    ) : (
                        <Loader2 className="text-[#5F5ADB] animate-spin" />
                    )}
                </div>
            </div>
        </div>
    );
};

export default PdfUpload;