# playwright

**Author:** hjlarry  
**Version:** 0.0.1  
**Type:** tool  
**Repo&Issue:** [https://github.com/hjlarry/dify-plugin-playwright](https://github.com/hjlarry/dify-plugin-playwright)  

A tool can be used to automate the browser with playwright script.

## Get Started

### 1. run your playwright server

The default port `3000` is already used by dify, you should change to another port.

**Option 1 (Use Docker)**
```
docker run -p 3003:3000 --rm --init -it --workdir /home/pwuser --user pwuser mcr.microsoft.com/playwright:v1.51.0-noble /bin/sh -c "npx -y playwright@1.51.0 run-server --port 3000 --host 0.0.0.0"
```

**Option 2 (Use npx)**
```
npx -y playwright@1.51.0 run-server --port 3003 --host 0.0.0.0
```

### 2. Authroize

Use `ws://<IP>:3003` to authorize.

### 3. Execute script
The script should like this:
```
page = browser.new_page(); page.goto('http://playwright.dev'); result = page.screenshot();
```
using `;` to separate commands. Assign the final output to the variable `result`(only support string and bytes). Utilize the `browser` variable to access the browser object. 

### 4. The agent can use this tool well
![agent](./_assets/agent.png)