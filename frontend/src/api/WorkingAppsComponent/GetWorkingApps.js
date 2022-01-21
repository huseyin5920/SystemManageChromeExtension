import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/showOpenWindow`

const WorkingApps = async () => {
    const response = await axios.get(
        url,
    )
    return response.data
}
export default WorkingApps
