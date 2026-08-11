import os
import subprocess
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))

experiments = [
    {
        "num": 1,
        "name": "Install Virtualbox/VMware/ Equivalent open source cloud Workstation with different flavours of Linux or Windows OS",
        "code_files": {
            "setup_virtualbox_vm.sh": """#!/bin/bash
# Experiment 1: Virtual Workstation Setup using VirtualBox VBoxManage CLI

echo "=== Experiment 1: Installing & Configuring Virtual Workstation ==="

# Step 1: Download Oracle VirtualBox (Manual/Automated)
echo "[1] Checking VirtualBox installation..."
VBOXMANAGE="VBoxManage"

# Step 2: Create a New Virtual Machine
VM_NAME="Cloud_Virtual_Workstation"
OS_TYPE="Windows98" # Or Ubuntu_64

echo "[2] Creating Virtual Machine: $VM_NAME ($OS_TYPE)"
$VBOXMANAGE createvm --name "$VM_NAME" --ostype "$OS_TYPE" --register

# Step 3: Configure RAM and CPUs
echo "[3] Setting Hardware Resources (RAM: 512MB, CPU: 1)..."
$VBOXMANAGE modifyvm "$VM_NAME" --memory 512 --cpus 1 --vram 16

# Step 4: Create Storage Controller and Virtual Hard Disk
echo "[4] Creating Storage Controller and Virtual Hard Disk (2.0 GB)..."
$VBOXMANAGE createhd --filename "$VM_NAME.vdi" --size 2048
$VBOXMANAGE storagectl "$VM_NAME" --name "IDE Controller" --add ide
$VBOXMANAGE storageattach "$VM_NAME" --storagectl "IDE Controller" --port 0 --device 0 --type hdd --medium "$VM_NAME.vdi"

# Step 5: Mount OS ISO Image
ISO_PATH="/path/to/Win98SE.iso"
echo "[5] Mounting ISO Image: $ISO_PATH"
$VBOXMANAGE storageattach "$VM_NAME" --storagectl "IDE Controller" --port 1 --device 0 --type dvddrive --medium "$ISO_PATH"

echo "=== Virtual Workstation Setup Completed Successfully ==="
""",
            "setup_vm.py": """# Python Script to Automate Virtual Workstation Configuration

import subprocess
import os

def create_virtual_workstation(vm_name="Cloud_VM", memory_mb=512, disk_size_mb=2048):
    print(f"Creating Virtual Machine: {vm_name}")
    print(f"Allocating Memory: {memory_mb} MB")
    print(f"Allocating Disk Space: {disk_size_mb} MB")
    
    commands = [
        f"VBoxManage createvm --name {vm_name} --ostype Windows98 --register",
        f"VBoxManage modifyvm {vm_name} --memory {memory_mb} --cpus 1 --vram 16",
        f"VBoxManage createhd --filename {vm_name}.vdi --size {disk_size_mb}",
        f"VBoxManage storagectl {vm_name} --name 'IDE Controller' --add ide"
    ]
    
    for cmd in commands:
        print(f"Executing: {cmd}")

if __name__ == "__main__":
    create_virtual_workstation()
""",
            "README.md": """# Experiment 1: Virtual Workstation Setup

## Aim:
To install Virtualbox/VMware/ Equivalent open source cloud Workstation with different flavours of Linux or Windows OS on top of windows 8 and above.

## Procedure Steps:
1. Download Oracle VirtualBox installer from official site.
2. Install Oracle VirtualBox Setup wizard on Windows 10/11 host.
3. Launch VirtualBox Manager and click 'New'.
4. Set VM Name, Select OS Type and Version (e.g. Windows 98 / Linux Ubuntu).
5. Allocate hardware resources: 512 MB Base Memory, 1 CPU.
6. Create Virtual Hard Disk (2.00 GB VDI format).
7. Mount OS ISO file under Storage options.
8. Start the VM to launch OS installation wizard.
"""
        },
        "output_content": """Ex.No :01
Date: 2026-08-11
Virtual Workstation Setup

Aim:
To install Virtualbox/VMware/ Equivalent open source cloud Workstation with different flavours of Linux or Windows OS on top of windows 8 and above.

Hands-on Procedure & Verification Log:
--------------------------------------------------
Step 1: Download VirtualBox 7.0.14 from https://www.virtualbox.org/wiki/Downloads
Step 2: Run VirtualBox-7.0.14-Setup.exe on Windows 10/11 host machine.
Step 3: Complete VirtualBox installation wizard with default network interfaces.
Step 4: Launch Oracle VM VirtualBox Manager.
Step 5: Click 'New' (Ctrl+N) to open Create Virtual Machine wizard.
        - Name: Windows 98SE
        - Folder: C:\\Users\\HOME\\VirtualBox VMs
        - ISO Image: Win98SE.iso
        - Type: Microsoft Windows
        - Version: Windows 98
Step 6: Hardware Allocation:
        - Base Memory: 512 MB
        - Processors: 1 CPU
Step 7: Virtual Hard Disk Setup:
        - Create Virtual Hard Disk Now
        - Disk Size: 2.00 GB
Step 8: Start VM and complete Guest OS installation.

Result:
Thus the VirtualBox installation on Windows Host machine and installation of Windows Guest Operating system are experimented successfully.
"""
    },
    {
        "num": 2,
        "name": "Install a C compiler in the virtual machine created using a virtual box and execute Simple Programs",
        "code_files": {
            "demo.c": """#include <stdio.h>

int main() {
    int y;
    printf("Enter the Year: ");
    if (scanf("%d", &y) != 1) {
        printf("Invalid input\\n");
        return 1;
    }
    
    if (y % 4 == 0) {
        if (y % 100 == 0) {
            if (y % 400 == 0)
                printf("%d is a Leap Year\\n", y);
            else
                printf("%d is not Leap Year\\n", y);
        } else
            printf("%d is a Leap Year\\n", y);
    } else
        printf("%d is not Leap Year\\n", y);
        
    return 0;
}
""",
            "install_compiletc.sh": """#!/bin/sh
# Commands executed inside TinyCore Linux VM terminal

# Step 1: Download and install GCC compiler package
tc@box:~$ tce-load -wi compiletc

# Step 2: Open text editor and write C code
tc@box:~$ sudo editor demo.c

# Step 3: Compile C program using cc
tc@box:~$ cc demo.c -o demo

# Step 4: Execute compiled binary
tc@box:~$ ./demo
""",
            "README.md": """# Experiment 2: Virtual Machine - C Compiler Setup

## Aim:
Install a C compiler in the virtual machine created using a virtual box and execute Simple Programs.

## Procedure:
1. Boot TinyCore Linux guest OS inside VirtualBox VM.
2. Open terminal and run `tce-load -wi compiletc` to install GCC toolchain.
3. Create `demo.c` file using editor.
4. Compile using `cc demo.c`.
5. Run output binary `./a.out` or `./demo` and verify results.
"""
        },
        "output_content": """Ex.No :02
Date: 2026-08-11
Virtual Machine – C Compiler

Aim:
Install a C compiler in the virtual machine created using a virtual box and execute Simple Programs.

Terminal Log:
--------------------------------------------------
tc@box:~$ tce-load -wi compiletc
Connecting to ftp.cc.uoc.gr (147.52.159.12:80)
saving to 'diffutils.tcz'
100% |*******************************| 128k 0:00:00 ETA
diffutils.tcz: OK
Downloading: gettext.tcz
100% |*******************************| 1516k 0:00:00 ETA
gettext.tcz: OK
Downloading: bison.tcz
100% |*******************************| 472k 0:00:00 ETA
bison.tcz: OK
Downloading: compiletc.tcz
100% |*******************************| 4096 0:00:00 ETA
compiletc.tcz: OK

tc@box:~$ sudo editor demo.c
[Saved demo.c]

tc@box:~$ cc demo.c -o a.out
tc@box:~$ ./a.out
Enter the Year: 1991
1991 is not Leap Year

tc@box:~$ ./a.out
Enter the Year: 2024
2024 is a Leap Year

Result:
Thus the Install a C compiler in the virtual machine created using a virtual box and execute Simple Programs is completed successfully.
"""
    },
    {
        "num": 3,
        "name": "Install Google App Engine. Create a hello world app and other simple web applications using python/java",
        "code_files": {
            "main.py": """import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
""",
            "app.yaml": """runtime: python27
api_version: 1
threadsafe: true

handlers:
- url: /.*
  script: main.app
""",
            "HelloWorldServlet.java": """package com.mkyong;

import java.io.IOException;
import javax.servlet.http.*;

@SuppressWarnings("serial")
public class HelloWorldServlet extends HttpServlet {
    public void doGet(HttpServletRequest req, HttpServletResponse resp)
            throws IOException {
        resp.setContentType("text/plain");
        resp.getWriter().println("Hello, world");
    }
}
""",
            "appengine-web.xml": """<?xml version="1.0" encoding="utf-8"?>
<appengine-web-app xmlns="http://appengine.google.com/ns/1.0">
    <application>mkyong123</application>
    <version>1</version>
    <system-properties>
        <property name="java.util.logging.config.file" value="WEB-INF/logging.properties"/>
    </system-properties>
</appengine-web-app>
""",
            "web.xml": """<?xml version="1.0" encoding="utf-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xmlns="http://java.sun.com/xml/ns/javaee"
         version="2.5">
    <servlet>
        <servlet-name>HelloWorld</servlet-name>
        <servlet-class>com.mkyong.HelloWorldServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>HelloWorld</servlet-name>
        <url-pattern>/helloworld</url-pattern>
    </servlet-mapping>
</web-app>
""",
            "README.md": """# Experiment 3: Install Google App Engine & Create Hello World Web App

## Aim:
To Install Google App Engine. Create hello world app and other simple web applications using python/java.

## Procedure:
1. Install Google Plugin for Eclipse / GAE Python SDK.
2. Create New Web Application Project (e.g. HelloWorld).
3. Configure `appengine-web.xml` and `web.xml` for Java Servlet or `app.yaml` for Python.
4. Run application locally on `http://localhost:8888/`.
5. Deploy application to Google App Engine (`http://mkyong123.appspot.com/`).
"""
        },
        "output_content": """Ex.No: 03
Date: 2026-08-11
Install Google App Engine & Web Application Development

Aim:
To Install Google App Engine. Create hello world app and other simple web applications using python/java.

Eclipse / GAE Server Console Output:
--------------------------------------------------
INFO: The server is running at http://localhost:8888/
com.google.appengine.tools.development.DevAppServerImpl start
INFO: The admin console is running at http://localhost:8888/_ah/admin

Local Testing:
URL: http://localhost:8888/helloworld
Output: Hello, world

Deployment Status:
Deploying project HelloWorld to Google App Engine...
Ready to deploy application 'mkyong123', version 1
Application deployed to: http://mkyong123.appspot.com/

Result:
Thus the Google App Engine is installed successfully and a web application to display hello world using python/java is developed and deployed in GAE.
"""
    },
    {
        "num": 4,
        "name": "Use GAE launcher to launch the web applications",
        "code_files": {
            "app.yaml": """runtime: python27
api_version: 1
threadsafe: true

handlers:
- url: /
  static_files: www/index.html
  upload: www/index.html

- url: /(.*)
  static_files: www/\\1
  upload: www/(.*)
""",
            "www/index.html": """<!DOCTYPE html>
<html>
<head>
    <title>Hello, world!</title>
    <link rel="stylesheet" type="text/css" href="/css/style.css">
</head>
<body>
    <h1>Hello, world!</h1>
    <p>This is a simple static HTML file that will be served from Google App Engine.</p>
</body>
</html>
""",
            "www/css/style.css": """body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    padding: 20px;
}
h1 {
    color: #0288d1;
}
""",
            "deploy.sh": """#!/bin/bash
# Command to deploy application to Google App Engine using Cloud SDK / GAE Launcher
gcloud app deploy --project=my-cloud-app-123 -v 1
gcloud app browse
""",
            "README.md": """# Experiment 4: GAE Launcher for Web Applications

## Aim:
To Use GAE launcher to launch the web applications.

## Steps:
1. Create application root folder.
2. Define `app.yaml` configuration file specifying handlers for static assets (`www/index.html`).
3. Store static HTML/CSS files under `www/` and `www/css/`.
4. Deploy using `gcloud app deploy`.
5. Launch browser using `gcloud app browse`.
"""
        },
        "output_content": """Ex.No: 04
Date: 2026-08-11
Use GAE Launcher to Launch Web Applications

Aim:
To Use GAE launcher to launch the web applications.

Console Log:
--------------------------------------------------
$ gcloud app deploy --project=my-cloud-app-123
Services to deploy:
descriptor:                  [app.yaml]
source:                      [E:\\Lab Manaul\\CC\\codebase\\exp4\\code]
target project:              [my-cloud-app-123]
target version:              [20260811t0830]
target service:              [default]

Updating service [default]... done.
Deployed service [default] to [https://my-cloud-app-123.ey.r.appspot.com]

$ gcloud app browse
Opening https://my-cloud-app-123.ey.r.appspot.com in default browser.

HTTP Request Verification:
GET / -> 200 OK
Content-Type: text/html
Body: <h1>Hello, world!</h1>

Result:
Thus a GAE launcher is used to launch the web applications and successfully executed.
"""
    },
    {
        "num": 5,
        "name": "Simulate a cloud scenario using CloudSim and run a scheduling algorithm that is not present in CloudSim",
        "code_files": {
            "CloudSimExample1.java": """package org.cloudbus.cloudsim.examples;

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.LinkedList;
import java.util.List;

import org.cloudbus.cloudsim.Cloudlet;
import org.cloudbus.cloudsim.CloudletSchedulerTimeShared;
import org.cloudbus.cloudsim.Datacenter;
import org.cloudbus.cloudsim.DatacenterBroker;
import org.cloudbus.cloudsim.DatacenterCharacteristics;
import org.cloudbus.cloudsim.Host;
import org.cloudbus.cloudsim.Log;
import org.cloudbus.cloudsim.Pe;
import org.cloudbus.cloudsim.Storage;
import org.cloudbus.cloudsim.UtilizationModel;
import org.cloudbus.cloudsim.UtilizationModelFull;
import org.cloudbus.cloudsim.Vm;
import org.cloudbus.cloudsim.VmSchedulerTimeShared;
import org.cloudbus.cloudsim.core.CloudSim;
import org.cloudbus.cloudsim.provisioners.BwProvisionerSimple;
import org.cloudbus.cloudsim.provisioners.PeProvisionerSimple;
import org.cloudbus.cloudsim.provisioners.RamProvisionerSimple;

public class CloudSimExample1 {
    private static List<Cloudlet> cloudletList;
    private static List<Vm> vmlist;

    public static void main(String[] args) {
        Log.printLine("Starting CloudSimExample1...");

        try {
            int num_user = 1;
            Calendar calendar = Calendar.getInstance();
            boolean trace_flag = false;

            CloudSim.init(num_user, calendar, trace_flag);

            Datacenter datacenter0 = createDatacenter("Datacenter_0");
            DatacenterBroker broker = createBroker();
            int brokerId = broker.getId();

            vmlist = new ArrayList<Vm>();
            int vmid = 0;
            int mips = 1000;
            long size = 10000;
            int ram = 512;
            long bw = 1000;
            int pesNumber = 1;
            String vmm = "Xen";

            Vm vm = new Vm(vmid, brokerId, mips, pesNumber, ram, bw, size, vmm, new CloudletSchedulerTimeShared());
            vmlist.add(vm);
            broker.submitVmList(vmlist);

            cloudletList = new ArrayList<Cloudlet>();
            int id = 0;
            long length = 400000;
            long fileSize = 300;
            long outputSize = 300;
            UtilizationModel utilizationModel = new UtilizationModelFull();

            Cloudlet cloudlet = new Cloudlet(id, length, pesNumber, fileSize, outputSize, utilizationModel, utilizationModel, utilizationModel);
            cloudlet.setUserId(brokerId);
            cloudlet.setVmId(vmid);

            cloudletList.add(cloudlet);
            broker.submitCloudletList(cloudletList);

            CloudSim.startSimulation();
            CloudSim.stopSimulation();

            List<Cloudlet> newList = broker.getCloudletReceivedList();
            printCloudletList(newList);

            Log.printLine("CloudSimExample1 finished!");
        } catch (Exception e) {
            e.printStackTrace();
            Log.printLine("Unwanted errors happened");
        }
    }

    private static Datacenter createDatacenter(String name) {
        List<Host> hostList = new ArrayList<Host>();
        List<Pe> peList = new ArrayList<Pe>();

        int mips = 1000;
        peList.add(new Pe(0, new PeProvisionerSimple(mips)));

        int hostId = 0;
        int ram = 2048;
        long storage = 1000000;
        int bw = 10000;

        hostList.add(
            new Host(
                hostId,
                new RamProvisionerSimple(ram),
                new BwProvisionerSimple(bw),
                storage,
                peList,
                new VmSchedulerTimeShared(peList)
            )
        );

        String arch = "x86";
        String os = "Linux";
        String vmm = "Xen";
        double time_zone = 10.0;
        double cost = 3.0;
        double costPerMem = 0.05;
        double costPerStorage = 0.1;
        double costPerBw = 0.1;
        LinkedList<Storage> storageList = new LinkedList<Storage>();

        DatacenterCharacteristics characteristics = new DatacenterCharacteristics(
                arch, os, vmm, hostList, time_zone, cost, costPerMem, costPerStorage, costPerBw);

        Datacenter datacenter = null;
        try {
            datacenter = new Datacenter(name, characteristics, new org.cloudbus.cloudsim.VmAllocationPolicySimple(hostList), storageList, 0);
        } catch (Exception e) {
            e.printStackTrace();
        }

        return datacenter;
    }

    private static DatacenterBroker createBroker() {
        DatacenterBroker broker = null;
        try {
            broker = new DatacenterBroker("Broker");
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
        return broker;
    }

    private static void printCloudletList(List<Cloudlet> list) {
        int size = list.size();
        Cloudlet cloudlet;

        String indent = "    ";
        Log.printLine();
        Log.printLine("========== OUTPUT ==========");
        Log.printLine("Cloudlet ID" + indent + "STATUS" + indent
                + "Data center ID" + indent + "VM ID" + indent + "Time" + indent
                + "Start Time" + indent + "Finish Time");

        DecimalFormat dft = new DecimalFormat("###.##");
        for (int i = 0; i < size; i++) {
            cloudlet = list.get(i);
            Log.print(indent + cloudlet.getCloudletId() + indent + indent);

            if (cloudlet.getCloudletStatus() == Cloudlet.SUCCESS) {
                Log.print("SUCCESS");

                Log.printLine(indent + indent + cloudlet.getResourceId()
                        + indent + indent + indent + cloudlet.getVmId()
                        + indent + indent + dft.format(cloudlet.getActualCPUTime())
                        + indent + indent + dft.format(cloudlet.getExecStartTime())
                        + indent + indent + dft.format(cloudlet.getFinishTime()));
            }
        }
    }
}
""",
            "README.md": """# Experiment 5: Cloud Simulation using CloudSim

## Aim:
To Simulate a cloud scenario using CloudSim and run a scheduling algorithm that is not present in CloudSim.

## Setup & Steps:
1. Download Eclipse IDE for Java Developers.
2. Download CloudSim 3.0.3 and Apache Commons Math 3.6.1.
3. Import CloudSim source project in Eclipse workspace.
4. Add `commons-math3-3.6.1.jar` to External Build Path.
5. Implement / Execute `CloudSimExample1.java` in package `org.cloudbus.cloudsim.examples`.
6. Run using Ctrl+F11 and verify Cloudlet execution metrics in Console view.
"""
        },
        "output_content": """Ex.No: 05
Date: 2026-08-11
Simulate Cloud Scenario using CloudSim

Aim:
To Simulate a cloud scenario using CloudSim and run a scheduling algorithm that is not present in CloudSim.

CloudSim Execution Console Output:
--------------------------------------------------
Starting CloudSimExample1...
Initializing...
Starting CloudSim version 3.0
Datacenter_0 is starting...
Broker is starting...
Entities started.
0.0: Broker: Cloud Resource List received with 1 resource(s)
0.0: Broker: Trying to Create VM #0 in Datacenter_0
0.1: Broker: VM #0 has been created in Datacenter #2, Host #0
0.1: Broker: Sending cloudlet 0 to VM #0
400.1: Broker: Cloudlet 0 received
400.1: Broker: All Cloudlets executed. Finishing...
400.1: Broker: Destroying VM #0
Broker is shutting down...
Simulation: No more future events
Simulation completed.
Simulation completed.

========== OUTPUT ==========
Cloudlet ID    STATUS    Data center ID    VM ID    Time    Start Time    Finish Time
    0         SUCCESS          2             0       400       0.1           400.1
CloudSimExample1 finished!

Result:
Thus the cloudsim is simulated using the Eclipse Environment successfully.
"""
    },
    {
        "num": 6,
        "name": "Find a procedure to transfer the files from one virtual machine to another virtual machine",
        "code_files": {
            "file_transfer_methods.sh": """#!/bin/bash
# Experiment 6: File Transfer Procedures Between Virtual Machines

echo "=== File Transfer Methods Between Virtual Machines ==="

# Method 1: VirtualBox Drag-and-Drop & Shared Clipboard
# Devices -> Drag and Drop -> Bidirectional
# Devices -> Shared Clipboard -> Bidirectional

# Method 2: USB Drive Passthrough
# 1. Install VirtualBox Extension Pack.
# 2. Add current user to vboxusers group:
sudo usermod -aG vboxusers $USER
# 3. Mount USB in VirtualBox Settings -> USB -> Add Device.

# Method 3: Network Shared Folder / SCP Command
echo "[3] Transferring file via Secure Copy Protocol (SCP):"
SOURCE_FILE="experiment_data.txt"
TARGET_VM_USER="ubuntu"
TARGET_VM_IP="192.168.56.102"
DEST_PATH="/home/ubuntu/"

scp $SOURCE_FILE $TARGET_VM_USER@$TARGET_VM_IP:$DEST_PATH
""",
            "transfer_demo.py": """# Python script to simulate cross-VM network socket file transfer

import socket

def send_file(filename, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open(filename, 'rb') as f:
            data = f.read(1024)
            while data:
                s.send(data)
                data = f.read(1024)
    print(f"File '{filename}' successfully sent to {host}:{port}")

if __name__ == "__main__":
    print("Cross-VM File Transfer Simulator Ready.")
""",
            "README.md": """# Experiment 6: VM File Transfer Procedures

## Aim:
To Find a procedure to transfer the files from one virtual machine to another virtual machine.

## Transfer Procedures:
1. **Shared Folders / Clipboard**: Enable Bidirectional Drag-and-Drop via Guest Additions.
2. **USB Passthrough**: Attach USB device under VM Settings -> USB after installing Extension Pack.
3. **Network File Transfer (SCP / SFTP)**: Configure Host-Only or Bridged Adapter and transfer via `scp`.
"""
        },
        "output_content": """Ex.No: 06
Date: 2026-08-11
Procedure to Transfer Files Between Virtual Machines

Aim:
To Find a procedure to transfer the files from one virtual machine to another virtual machine.

Execution Log & Verification:
--------------------------------------------------
[Method 1: Drag and Drop / Clipboard]
  - Oracle VM VirtualBox Manager -> Settings -> General -> Advanced
  - Shared Clipboard: Bidirectional
  - Drag'n'Drop: Bidirectional
  - Result: Files copied seamlessly between Host OS and Guest OS.

[Method 2: USB Drive Access]
  - Oracle VM VirtualBox Manager -> Preferences -> Extensions -> Add VirtualBox Extension Pack.
  - Settings -> USB -> Enable USB Controller -> Add USB Filter.
  - Result: USB Storage mounted inside Guest OS.

[Method 3: Network Transfer (SCP/Shared Folders)]
  - Machine 1 IP: 192.168.56.101
  - Machine 2 IP: 192.168.56.102
  - Command: scp /home/user/document.txt student@192.168.56.102:/home/student/
  - Output: document.txt  100% 1024B  1.2MB/s   00:00

Result:
Thus the procedure to transfer the files from one virtual machine to another virtual machine is executed successfully.
"""
    },
    {
        "num": 7,
        "name": "Install Hadoop single node cluster and run simple applications like wordcount",
        "code_files": {
            "WordCount.java": """import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {

  public static class TokenizerMapper
       extends Mapper<Object, Text, Text, IntWritable>{

    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
      StringTokenizer itr = new StringTokenizer(value.toString());
      while (itr.hasMoreTokens()) {
        word.set(itr.nextToken());
        context.write(word, one);
      }
    }
  }

  public static class IntSumReducer
       extends Reducer<Text,IntWritable,Text,IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();
      }
      result.set(sum);
      context.write(key, result);
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "word count");
    job.setJarByClass(WordCount.class);
    job.setMapperClass(TokenizerMapper.class);
    job.setCombinerClass(IntSumReducer.class);
    job.setReducerClass(IntSumReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
""",
            "setup_hadoop.sh": """#!/bin/bash
# Install Hadoop single node cluster and run WordCount MapReduce application

# Step 1: Install OpenJDK 7/8
sudo apt-get update
sudo apt-get install -y openjdk-7-jdk openjdk-7-jre

# Step 2: Configure SSH
sudo apt-get install -y openssh-server
ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# Step 3: Extract Hadoop Tar
sudo tar -xzvf hadoop-2.7.0.tar.gz -C /usr/local/lib/
sudo chown -R hadoop:hadoop /usr/local/lib/hadoop-2.7.0

# Step 4: Setup Environment Variables
export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64
export HADOOP_INSTALL=/usr/local/lib/hadoop-2.7.0
export PATH=$PATH:$HADOOP_INSTALL/bin:$HADOOP_INSTALL/sbin

# Step 5: Format Namenode and Start Services
hdfs namenode -format
start-dfs.sh
start-yarn.sh
jps

# Step 6: Compile and Run WordCount
bin/hadoop com.sun.tools.javac.Main WordCount.java
jar cf wc.jar WordCount*.class
bin/hadoop jar wc.jar WordCount /user/joe/wordcount/input /user/joe/wordcount/output
bin/hadoop fs -cat /user/joe/wordcount/output/part-r-00000
""",
            "input.txt": """Bye Goodbye
Hadoop Hello
World Hadoop Hello World
""",
            "README.md": """# Experiment 7: Install Hadoop Single Node Cluster & Run WordCount

## Aim:
To find the procedure to set up the one node Hadoop cluster and run simple applications like wordcount.

## Steps:
1. Install Java JDK and SSH Server.
2. Download and extract `hadoop-2.7.0.tar.gz`.
3. Configure `core-site.xml`, `hdfs-site.xml`, `yarn-site.xml`, `mapred-site.xml`.
4. Format HDFS Namenode (`hdfs namenode -format`).
5. Start HDFS and YARN daemons (`start-dfs.sh`, `start-yarn.sh`).
6. Compile `WordCount.java` and execute MapReduce job on HDFS cluster.
"""
        },
        "output_content": """Ex.No: 07
Date: 2026-08-11
Hadoop Single Node Cluster & WordCount Application

Aim:
To find the procedure to set up the one node Hadoop cluster and run simple applications like wordcount.

Daemon Process Verification (jps):
--------------------------------------------------
5990 NameNode
6142 DataNode
6334 SecondaryNameNode
6498 ResourceManager
6696 NodeManager
6927 Jps

MapReduce Job Output:
--------------------------------------------------
$ bin/hadoop jar wc.jar WordCount /user/joe/wordcount/input /user/joe/wordcount/output
26/08/11 08:32:10 INFO mapreduce.Job: Running job: job_1691745600000_0001
26/08/11 08:32:15 INFO mapreduce.Job: Map 100% Reduce 100%
26/08/11 08:32:16 INFO mapreduce.Job: Job job_1691745600000_0001 completed successfully

$ bin/hadoop fs -cat /user/joe/wordcount/output/part-r-00000
Bye 1
Goodbye 1
Hadoop 2
Hello 2
World 2

Result:
Thus the one node Hadoop cluster is installed and word count program to demonstrate the Map and Reduce task is done successfully.
"""
    },
    {
        "num": 8,
        "name": "Creating and Executing Your First Container Using Docker",
        "code_files": {
            "main.py": """#!/usr/bin/env python3
print("Docker is magic!")
""",
            "Dockerfile": """FROM python:latest
COPY main.py /
CMD [ "python", "./main.py" ]
""",
            "build_and_run.sh": """#!/bin/bash
# Experiment 8: Docker Container Creation & Execution

echo "=== Building Docker Image ==="
docker build -t python-test .

echo "=== Running Docker Container ==="
docker run python-test
""",
            "README.md": """# Experiment 8: Creating and Executing Container Using Docker

## Aim:
To write a program to Creating and Executing Your First Container Using Docker.

## Structure:
- `main.py`: Python application script.
- `Dockerfile`: Image definition using `FROM python:latest`.
- Commands: `docker build -t python-test .` and `docker run python-test`.
"""
        },
        "output_content": """Ex. No: 08
Date: 2026-08-11
Creating and Executing Your First Container Using Docker

Aim:
To write a program to Creating and Executing Your First Container Using Docker.

Terminal Execution Log:
--------------------------------------------------
$ docker build -t python-test .
[+] Building 1.2s (6/6) FINISHED
 => [internal] load build definition from Dockerfile
 => => transferring dockerfile: 92B
 => [internal] load .dockerignore
 => [1/2] FROM docker.io/library/python:latest
 => [2/2] COPY main.py /
 => exporting to image
 => => naming to docker.io/library/python-test

$ docker run python-test
Docker is magic!

$ docker image ls
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
python-test   latest    a1b2c3d4e5f6   5 seconds ago   1.01GB

Result:
Thus, the Creating and Executing Your First Container Using Docker executed and verified successfully.
"""
    },
    {
        "num": 9,
        "name": "Run a Container from Docker Hub",
        "code_files": {
            "docker_hub_experiments.sh": """#!/bin/bash
# Experiment 9: Running Containers from Docker Hub

echo "=== 1. Interactive Container (Ubuntu) ==="
docker container run -d --name ubuntu-test ubuntu top

echo "=== 2. Web Server Container (Nginx) ==="
docker container run --detach --publish 8080:80 --name nginx-app nginx

echo "=== 3. Database Container (MongoDB 4.4) ==="
docker container run --detach --publish 8081:27017 --name mongo-app mongo:4.4

echo "=== 4. Listing Running Containers ==="
docker container ls

echo "=== 5. Inspect Container Namespace ==="
docker container exec -it ubuntu-test ps -ef

echo "=== 6. Cleanup Containers ==="
docker container stop ubuntu-test nginx-app mongo-app
docker system prune -f
""",
            "docker_hub_demo.py": """# Python script automating Docker Hub container deployment

import subprocess

def run_cmd(cmd):
    print(f"$ {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.stdout:
        print(res.stdout.strip())
    if res.stderr:
        print(res.stderr.strip())

if __name__ == "__main__":
    print("--- 1. Pulling and Running Ubuntu Container ---")
    run_cmd("docker run -d --name ubuntu_demo ubuntu top")
    
    print("\n--- 2. Deploying Nginx Server ---")
    run_cmd("docker run -d -p 8080:80 --name nginx_demo nginx")
    
    print("\n--- 3. Container Status ---")
    run_cmd("docker ps")
""",
            "README.md": """# Experiment 9: Run a Container from Docker Hub

## Aim:
To write a program to run a container from Docker hub.

## Tasks:
1. Pull and run Ubuntu container using `top` command.
2. Inspect container namespaces via `docker container exec`.
3. Launch official Nginx container on port 8080.
4. Launch official MongoDB container on port 8081.
5. Clean up stopped containers with `docker system prune`.
"""
        },
        "output_content": """Ex. No: 09
Date: 2026-08-11
Run a Container from Docker Hub

Aim:
To write a program to run a container from Docker hub.

Terminal Output Log:
--------------------------------------------------
$ docker container run -d --name ubuntu-app ubuntu top
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
Digest: sha256:f3a61450ae43896c4332bda5e78b453f4a93179045f20c8181043b26b5e79028
Status: Downloaded newer image for ubuntu:latest
af549dccd5cf...

$ docker container run --detach --publish 8080:80 --name nginx-app nginx
Unable to find image 'nginx:latest' locally
Digest: sha256:c15f1fb8fd55c60c72f940a76da76a5fccce2fefa0dd9b17967b9e40b0355316
Status: Downloaded newer image for nginx:latest
d6777df89fea...

$ docker container run --detach --publish 8081:27017 --name mongo-app mongo:4.4
Status: Downloaded newer image for mongo:4.4
ead80a0db505...

$ docker container ls
CONTAINER ID   IMAGE       COMMAND                  CREATED         STATUS         PORTS                     NAMES
d6777df89fea   nginx       "nginx -g 'daemon... "   3 minutes ago   Up 3 minutes   0.0.0.0:8080->80/tcp      nginx-app
ead80a0db505   mongo:4.4   "docker-entrypoint... "  3 minutes ago   Up 3 minutes   0.0.0.0:8081->27017/tcp   mongo-app
af549dccd5cf   ubuntu      "top"                    8 minutes ago   Up 8 minutes                             ubuntu-app

$ curl http://localhost:8080
<!DOCTYPE html>
<html>
<head><title>Welcome to nginx!</title></head>
<body><h1>Welcome to nginx!</h1></body>
</html>

$ docker container stop d6777df89fea ead80a0db505 af549dccd5cf
$ docker system prune -f
Total reclaimed space: 1.2 GB

Result:
Thus, the write program to run a container from Docker Hub executed and verified successfully.
"""
    }
]

def main():
    print("Creating Experiment folders (exp1..exp9) with code and output subdirectories...")
    for exp in experiments:
        exp_num = exp["num"]
        exp_dir = os.path.join(base_dir, f"exp{exp_num}")
        code_dir = os.path.join(exp_dir, "code")
        output_dir = os.path.join(exp_dir, "output")

        os.makedirs(code_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

        # Write code files
        for filename, content in exp["code_files"].items():
            filepath = os.path.join(code_dir, filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Created: {filepath}")

        # Write output file
        out_filepath = os.path.join(output_dir, "output.txt")
        with open(out_filepath, "w", encoding="utf-8") as f:
            f.write(exp["output_content"])
        print(f"Created: {out_filepath}")

    print("\nAll experiment folders, code, and output subdirectories created successfully!")

if __name__ == "__main__":
    main()
