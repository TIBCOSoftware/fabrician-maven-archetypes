#
# Copyright (c) 2013 TIBCO Software Inc. All Rights Reserved.
# 
# Use is subject to the terms of the TIBCO license terms accompanying the download of this code. 
# In most instances, the license terms are contained in a file named license.txt.
#

from com.datasynapse.fabric.admin.info import AllocationInfo
from com.datasynapse.fabric.util import GridlibUtils, ContainerUtils
from com.datasynapse.fabric.common import RuntimeContextVariable, ActivationInfo
import java.lang.System
from subprocess import call, Popen
import os
import platform
import time
import socket
import fnmatch

#
# This is an example enabler script using Jython 2.5
# 
# This application assumes the following
#   * It has a seperate data directory that can persist after the enabler shuts down. For example, on an NFS share
#   * It has a control binary in the bin directory that has 'start', 'stop', 'status' commands 
#   * The Engine runs as 'root', but the application runs as the RUNAS_USER.
#


def prepareWorkDirectory():
    proxy.prepareWorkDirectory()
  
def doInit(additionalVariables):
    logInfo("--------------------doInit------------------------------")
    workdir = runtimeContext.getVariable('CONTAINER_WORK_DIR').getValue()
    datadir = runtimeContext.getVariable('APP_DATA_DIR').getValue()
    basedir = runtimeContext.getVariable('APP_BASE_DIR').getValue() 
    runasuser = runtimeContext.getVariable('RUNAS_USER').getValue() 
  
    # Now add the user if not already there  
    logInfo("/usr/sbin/useradd " + runasuser)
    call(["/usr/sbin/useradd",runasuser])
    
    # And change the owner
    logInfo("chown dirs to " + runasuser)
    call(['chown','-R',runasuser, basedir]);
    
def doStart():
    logInfo("--------------------doStart------------------------------")
    basedir = runtimeContext.getVariable('APP_BASE_DIR').getValue() 
    datadir = runtimeContext.getVariable('APP_DATA_DIR').getValue()
    runasuser = runtimeContext.getVariable('RUNAS_USER').getValue() 
    if (not os.path.exists(datadir)) :
        logInfo("Data dir does not exist, creating and initializing: " + datadir)
        os.makedirs(datadir)
        call(['chown','-R',runasuser, datadir]);
        # do some initialization 
    else : 
        logInfo("Data directory already exists: " + datadir);

    # The files in 'content' will be in 'workdir' now. 
    # Copy any of those to the correct place in basedir or datadir as needed here

    # Start the app    
    callControlCommand('start', basedir, datadir, runasuser)
   
def doInstall(info):
    logInfo("--------------------doInstall------------------------------")

def doUninstall():
    logInfo("--------------------doUninstall------------------------------")
 
def doShutdown():
    logInfo("--------------------doShutdown------------------------------")
    basedir = runtimeContext.getVariable('APP_BASE_DIR').getValue() 
    datadir = runtimeContext.getVariable('APP_DATA_DIR').getValue()
    runasuser = runtimeContext.getVariable('RUNAS_USER').getValue() 
    callControlCommand('stop', basedir, datadir, runasuser)
    
# running condition
def getContainerRunningConditionPollPeriod():
    return 5000

def isContainerRunning():
    basedir = runtimeContext.getVariable('APP_BASE_DIR').getValue() 
    datadir = runtimeContext.getVariable('APP_DATA_DIR').getValue()
    runasuser = runtimeContext.getVariable('RUNAS_USER').getValue() 
    status = callControlCommand('status', basedir, datadir, runasuser)
    if status == 0:
        return True
    else:
        return False 
    
def getComponentRunningConditionErrorMessage():
    return "status returned nonzero"

def callControlCommand(cmd, basedir, datadir, runasuser):
    # set up the control command here, for example
    # command = os.path.join(basedir, "bin")
    # command = os.path.join(command, "app_ctl")
    # command = command + ' -D ' + datadir + ' ' + cmd 
    return callAsUser(command, runasuser)
    
    
def callAsUser(command, runasuser):
    logInfo('Executing command: ' + command)
    return call(['su','-c',command,runasuser])
    logInfo('Command finished')
    
# writes the message in the engine log
def logInfo(msg):
  logger.info(msg)

    

