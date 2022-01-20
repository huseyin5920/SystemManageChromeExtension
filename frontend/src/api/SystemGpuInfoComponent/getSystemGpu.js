import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/systemGpuInfo`

const GetSystemGpu = async () => {
    const response = await axios.get(
        url,

    )
    return response.data
}
export default GetSystemGpu
