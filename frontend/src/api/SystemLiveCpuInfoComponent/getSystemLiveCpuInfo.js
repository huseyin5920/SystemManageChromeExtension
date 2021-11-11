import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/systemLiveCpuInfo`

const GetSystemLiveCpuInfo = async () => {
    const response = await axios.get(
        url,

    )
    return response.data
}
export default GetSystemLiveCpuInfo
