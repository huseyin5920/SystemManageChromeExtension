import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/basicDiskInfo`

const GetDiskUsage = async () => {
    const response = await axios.get(
        url,
    )
    return response.data
}
export default GetDiskUsage
