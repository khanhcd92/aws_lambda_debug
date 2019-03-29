exports.handler = (event, context, callback) => {
    let region = process.env.REGION;
    console.log('region: ', region);
    callback(null, event);
};