(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[414],{2948:e=>{"use strict";e.exports="SECRET_DO_NOT_PASS_THIS_OR_YOU_WILL_BE_FIRED"},3265:(e,r,t)=>{"use strict";t.r(r),t.d(r,{default:()=>c});var s=t(5155),o=t(2115),a=t(8637);function n(e){let{title:r,author:t}=e;return(0,s.jsxs)("div",{className:"max-w-sm p-6 bg-white border border-gray-200 rounded-lg shadow-sm dark:bg-gray-800 dark:border-gray-700 flex flex-col",children:[(0,s.jsx)("div",{className:"w-full text-gray-700 dark:text-gray-400",children:(0,s.jsx)("p",{className:"font-medium truncate text-left",children:t})}),(0,s.jsx)("div",{className:"w-full mt-2",children:(0,s.jsx)("h3",{className:"text-2xl font-bold tracking-tight text-gray-900 dark:text-white text-left",children:r})}),(0,s.jsx)("div",{className:"w-full flex justify-end mt-5",children:(0,s.jsxs)("a",{href:"#",className:"inline-flex items-center px-3 py-2 text-sm font-medium text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",children:["Read more",(0,s.jsx)("svg",{className:"rtl:rotate-180 w-3.5 h-3.5 ms-2","aria-hidden":"true",xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 14 10",children:(0,s.jsx)("path",{stroke:"currentColor",strokeLinecap:"round",strokeLinejoin:"round",strokeWidth:"2",d:"M1 5h12m0 0L9 1m4 4L9 9"})})]})})]})}function l(e){let{books:r}=e;return r?0===r.length?(0,s.jsx)("div",{className:"bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mx-auto max-w-md mt-10",children:(0,s.jsx)("p",{children:"No books found."})}):(0,s.jsxs)("div",{className:"container mx-auto px-4 py-8",children:[(0,s.jsx)("h1",{className:"text-2xl font-bold mb-6",children:"Book Collection"}),(0,s.jsx)("div",{className:"grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6",children:r.map(e=>(0,s.jsx)(n,{title:e.title,author:e.author},e.id))})]}):(0,s.jsx)("div",{className:"flex justify-center items-center min-h-screen",children:(0,s.jsx)("div",{className:"animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"})})}l.propTypes={books:t.n(a)().array.isRequired};let i=async()=>{try{let e=await fetch("".concat("https://wbt2425.onrender.com","/book/available"));if(!e.ok)throw Error("HTTP error! Status: ".concat(e.status));return await e.json()}catch(e){throw console.error("Error fetching available books:",e),e}};function c(){let[e,r]=(0,o.useState)([]),[t,a]=(0,o.useState)(!0),[n,c]=(0,o.useState)(null);return((0,o.useEffect)(()=>{(async()=>{try{a(!0);let e=await i();r(e)}catch(e){c(e.message),console.error("Error fetching books:",e)}finally{a(!1)}})()},[]),t)?(0,s.jsx)("div",{className:"flex justify-center items-center min-h-screen",children:(0,s.jsx)("div",{className:"animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"})}):n?(0,s.jsxs)("div",{className:"bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mx-auto max-w-md mt-10",children:[(0,s.jsxs)("p",{children:["Error loading books: ",n]}),(0,s.jsx)("p",{children:"Please try again later"})]}):(0,s.jsx)(l,{books:e})}},7346:(e,r,t)=>{Promise.resolve().then(t.bind(t,3265))},8637:(e,r,t)=>{e.exports=t(9399)()},9399:(e,r,t)=>{"use strict";var s=t(2948);function o(){}function a(){}a.resetWarningCache=o,e.exports=function(){function e(e,r,t,o,a,n){if(n!==s){var l=Error("Calling PropTypes validators directly is not supported by the `prop-types` package. Use PropTypes.checkPropTypes() to call them. Read more at http://fb.me/use-check-prop-types");throw l.name="Invariant Violation",l}}function r(){return e}e.isRequired=e;var t={array:e,bigint:e,bool:e,func:e,number:e,object:e,string:e,symbol:e,any:e,arrayOf:r,element:e,elementType:e,instanceOf:r,node:e,objectOf:r,oneOf:r,oneOfType:r,shape:r,exact:r,checkPropTypes:a,resetWarningCache:o};return t.PropTypes=t,t}}},e=>{var r=r=>e(e.s=r);e.O(0,[441,684,358],()=>r(7346)),_N_E=e.O()}]);