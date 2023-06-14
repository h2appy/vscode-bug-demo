# Environments:
    MacBook with Apple M1 Max
    macOS 13.4
    VSCode:
        Version: 1.79.1 (Universal)
        Commit: 4cb974a7aed77a74c7813bdccd99ee0d04901215
        Date: 2023-06-12T16:16:49.215Z
        Electron: 22.5.7
        Chromium: 108.0.5359.215
        Node.js: 16.17.1
        V8: 10.8.168.25-electron.0
        OS: Darwin arm64 22.5.0
    Node.js v18.14.2
    Docker Desktop 4.20.0 (109717)

# Steps to Reproduce:


#### 1. Add breakpoints in files:
    * /project-a/app.py
        print("Add breakpoint here")
    * /project-b/app.py
        print("Add breakpoint here")
    * foo.py
        print("Add breakpoint here")

#### 2. Start containers

```bash
cd vscode-bug-demo
docker compose up
```

#### 3. Debug with "Python: Remote Attach to project-a"
The following warnings will be printed:

```bash
vscode-bug-demo-project-a-1  | 32.90s - pydev debugger: unable to find translation for: "/Users/johnny/workspaces/vscode-bug-demo/project-b/project-b/app.py" in ["/Users/johnny/workspaces/vscode-bug-demo/project-a/", "/Users/johnny/workspaces/vscode-bug-demo/project-a"] (please revise your path mappings).
vscode-bug-demo-project-a-1  | 
vscode-bug-demo-project-a-1  | 0.00s - pydev debugger: unable to find translation for: "/Users/johnny/workspaces/vscode-bug-demo/project-b/foo.py" in ["/Users/johnny/workspaces/vscode-bug-demo/project-a/", "/Users/johnny/workspaces/vscode-bug-demo/project-a"] (please revise your path mappings).
vscode-bug-demo-project-a-1  | 
vscode-bug-demo-project-a-1  | 32.99s - pydev debugger: unable to find translation for: "/Users/johnny/workspaces/vscode-bug-demo/project-b/project-b/app.py" in ["/Users/johnny/workspaces/vscode-bug-demo/project-a/", "/Users/johnny/workspaces/vscode-bug-demo/project-a"] (please revise your path mappings).
vscode-bug-demo-project-a-1  | 
vscode-bug-demo-project-a-1  | 0.00s - pydev debugger: unable to find translation for: "/Users/johnny/workspaces/vscode-bug-demo/project-b/foo.py" in ["/Users/johnny/workspaces/vscode-bug-demo/project-a/", "/Users/johnny/workspaces/vscode-bug-demo/project-a"] (please revise your path mappings).
vscode-bug-demo-project-a-1  |  
```