import axios from "axios"
import { ip } from "../URL"

let url = `${ip}/cpu`

const GetCpu = async () => {
  const response = await axios.get(
    url,

  )
  return JSON.parse(response.data.replaceAll("'", "\""))
}
export default GetCpu
