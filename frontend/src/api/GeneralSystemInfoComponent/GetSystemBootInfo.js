import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/systemBootInfo`

const GetSystemBootInfo = async () => {
    const response = await axios.get(
        url,

    )
    return response.data
}
export default GetSystemBootInfo
