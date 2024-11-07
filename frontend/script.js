const server_url = "http://127.0.0.1:5000/completion"

var waitingForResponse = false;
const waitRespMsg = "No momento uma requisição esta sendo processada. Por favor espere a resposta dessa requisição antes de enviar uma nova.\n\n" +
    "Geralmente o processamento não dura mais do que 1 minuto. Caso esteja esperando por mais tempo por favor recarregue a pagina.";

async function callApiFetch(url, bodyObj) {
    try {
        waitingForResponse = true;
        body = JSON.stringify(bodyObj)
        console.log("body =  "+ body)
    
        const resp = await fetch(url, {
            method : "POST",
            mode: 'cors',
            headers: {
                "Content-Type": "application/json",
            },
            body: body,
        });
        const respData = await resp.json();
        console.log("respData = " + respData);
        
        waitingForResponse = false;
        return respData;
    } catch (error) {
        console.log(error);
        waitingForResponse = false;
        return;
    } finally {
        waitingForResponse = false;
    }
}

// { "resource":"completion", "payload": 
//   { "context":"Sou Brasileiro.", 
//     "question":"Quanto imposto tenho que pagar sobre rendimentos de renda fixa?" 
// }}
async function submitPrompt() {
    if(waitingForResponse){
        alert(waitRespMsg);
        return;
    }
    const question = document.getElementById("question").value;
    const data = { question };
    /** 
     * 
  {
  "model": "GPT-4o",
  "messages": [
    {
      "role": "system",
      "content": "You're a lawyer"
    },
    {
      "role": "assistant",
      "content": "Can I smoke weed in Germany"
    }
  ]
}
     * 
    */
    const reqBody = { messages: [ { model:"GPT-4o", role: "system", content: "You're a lawyer" }, { role: "assistant", content: question } ] };
    console.log(" -- Completion : reqBody = " + JSON.stringify(reqBody))

    resp = await callApiFetch(server_url, reqBody)
    if(resp){
        document.getElementById("result").innerHTML += resp.response + "\n\n";
        // expand the textarea to fit the context text
        document.getElementById("result").style.height = document.getElementById("result").scrollHeight + "px";
    }else{
        console.error(error);
    }
}
