export const store={get:(k:string,d:any)=>{try{return JSON.parse(localStorage.getItem(k)||"null")??d}catch{return d}},set:(k:string,v:any)=>localStorage.setItem(k,JSON.stringify(v))};
