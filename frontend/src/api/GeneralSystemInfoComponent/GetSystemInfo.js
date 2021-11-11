import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/systemInfo`

const GetSystemInfo = async () => {
    const response = await axios.get(
        url,

    )
    return response.data
}
export default GetSystemInfo
