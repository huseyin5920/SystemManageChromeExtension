import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/systemCpuInfo`

const GetSystemCpu = async () => {
    const response = await axios.get(
        url,

    )
    return response.data
}
export default GetSystemCpu
