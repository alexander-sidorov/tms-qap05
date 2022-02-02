const buttonAdd = document.getElementById("id_add");
const buttonGetResult = document.getElementById("id_get_result");
const containerResult = document.getElementById("id_result_container");
const inputInt = document.getElementById("id_v_int");
const inputStr = document.getElementById("id_v_str");
const spanResult = document.getElementById("id_result");

const API = "/api/10/04";

document.addEventListener("DOMContentLoaded", setUp);


async function setUp() {
    buttonAdd.addEventListener("click", addValue);
    buttonGetResult.addEventListener("click", getResult);
    containerResult.style.display = "none";
}


async function addValue() {
    let data;

    if (inputInt.value !== "") {
        data = {"v_int": parseInt(inputInt.value)};
    } else if (inputStr.value !== "") {
        data = {"v_str": inputStr.value};
    } else {
        alert("нужно хотя бы одно значение");
        return;
    }

    const resp = await apiCall(API, {method: "POST", json: data});
    console.log(JSON.stringify(resp));

    inputInt.value = inputStr.value = "";
}


async function getResult() {
    const resp = await apiCall(API, {method: "GET"});
    console.log(JSON.stringify(resp));

    spanResult.innerText = resp.data;
    containerResult.style.display = "block";
}


async function apiCall(url, args = {}) {
    const headers = new Headers();

    headers.set("content-type", "application/json");

    let fetchArgs = {
        method: "GET",
        headers: headers,
        body: null,
    }

    if (args) {
        if (args.method) {
            fetchArgs.method = args.method;
            if (args.method !== "GET" && args.json) {
                fetchArgs.body = JSON.stringify(args.json);
            }
        }
    }

    const resp = await fetch(url, fetchArgs);

    return resp.json();
}
