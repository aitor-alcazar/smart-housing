import { useParams } from "react-router-dom";
export default function(){const {id}=useParams();return <div className='card'>Report placeholder for evaluation {id}. Use /evaluate to generate a report.</div>}
