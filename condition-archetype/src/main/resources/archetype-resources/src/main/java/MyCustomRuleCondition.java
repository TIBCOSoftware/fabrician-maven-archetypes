/*
 * Copyright (c) 2013 TIBCO Software Inc. All Rights Reserved.
 * 
 * Use is subject to the terms of the TIBCO license terms accompanying the download of this code. 
 * In most instances, the license terms are contained in a file named license.txt.
 */
package ${packageName};

import com.datasynapse.fabric.broker.userartifact.condition.AbstractCustomRuleCondition;

/**
 * Silver Fabric CustomRuleCondition class implementation.
 */
public class MyCustomRuleCondition extends AbstractCustomRuleCondition {

    public MyCustomRuleCondition() {}

    @Override
    public boolean isSatisfied() {
        return true;
    }
        
    @Override
    public String getDescription() {
        return "Hello from MyCustomCondition";
    }
}
