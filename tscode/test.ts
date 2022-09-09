const getMsg = (msg: string) => msg.repeat(2)

async function waitMoment() {
    await new Promise(resolve => setTimeout(resolve, 1000));
}

async function main() {
    let msg = getMsg("Hello ")
    await waitMoment()
    console.log(msg)
}

main()