In JavaScript classes, you need to always call super when defining the constructor of a subclass. All React component classes that have a constructor should start with a super(props) call.

When you call setState in a component, React automatically updates the child components inside of it too.


To collect data from multiple children, or to have two child components communicate with each other, you need to declare the shared state in their parent component instead. The parent component can pass the state back down to the children by using props; this keeps the child components in sync with each other and with the parent component.

The DOM <button> element’s onClick attribute has a special meaning to React because it is a built-in component. For custom components like Square, the naming is up to you. We could give any name to the Square’s onClick prop or Board’s handleClick method, and the code would work the same. In React, it’s conventional to use on[Event] names for props which represent events and handle[Event] for the methods which handle the events.

It’s strongly recommended that you assign proper keys whenever you build dynamic lists.

React will update only the properties mentioned in setState method leaving the remaining state as is

"props" stands for properties. Props are arguments passed into React components. Props are passed to components via HTML attributes.

