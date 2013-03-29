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
