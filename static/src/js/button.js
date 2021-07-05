odoo.define("vauxoo_webinar_widgets_odoo13.button", (require) => {

    console.log('Loaded!');
    console.warn('I am ready!');

    const { Widget, registry } = require('web.public.Widget');
    const Dialog = require('web.Dialog');

    // Define a public Web Widget
    const WidgetButton = Widget.extend{
        selector: '.js_class',
        // Define the mouse event to listen to in the Widget
        events: {
            // When the HTML element "button" is clicked invoke the Javascript function "clickEvent"
            'click button':'clickEvent',
        },
        start () {
            this._super(...arguments);
            // ClipboardJS allows you to copy the product's URL to the clipboard
            new ClipboardJS(this.el, {
                text: () => document.location.origin + this.el.dataset.url,
                /*text: () => {
                    console.warn('you are copying me!: ' + document.location.origin + this.el.dataset.url),
                    return document.location.origin + this.el.dataset.url
                }*/
            });
        },
        // "clickEvent" function which handles the "click" event on the "button" element
        clickEvent (ev) {
            Dialog.alert(
                this,
                'You have copied the URL of the product!',
                {
                    title: 'Success!!!'
                }
            )
            
        },
    };

    // Registry a public Web Widget
    registry.WidgetButton = WidgetButton;
});
