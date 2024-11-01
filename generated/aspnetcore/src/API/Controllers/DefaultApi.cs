/*
 * Financial Instrument Sample Polymorph
 *
 * This is the description.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: openwealth@synpulse.com
 * Generated by: https://openapi-generator.tech
 */

using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using Swashbuckle.AspNetCore.Annotations;
using Swashbuckle.AspNetCore.SwaggerGen;
using System.Text.Json;
using API.Attributes;
using API.Models;

namespace API.Controllers
{ 
    /// <summary>
    /// 
    /// </summary>
    [ApiController]
    public class DefaultApiController : ControllerBase
    { 
        /// <summary>
        /// This is a summary
        /// </summary>
        /// <remarks>This is a description.</remarks>
        /// <param name="instrumentId">Instrument ID Parameter.</param>
        /// <response code="200">get instrument by id.</response>
        /// <response code="400">Unexpected error</response>
        [HttpGet]
        [Route("/financial-instruments/{instrumentId}")]
        [ValidateModelState]
        [SwaggerOperation("GetInstrumentById")]
        [SwaggerResponse(statusCode: 200, type: typeof(FinancialInstrument), description: "get instrument by id.")]
        [SwaggerResponse(statusCode: 400, type: typeof(string), description: "Unexpected error")]
        public virtual IActionResult GetInstrumentById([FromRoute (Name = "instrumentId")][Required]string instrumentId)
        {

            //TODO: Uncomment the next line to return response 200 or use other options such as return this.NotFound(), return this.BadRequest(..), ...
            // return StatusCode(200, default(FinancialInstrument));
            //TODO: Uncomment the next line to return response 400 or use other options such as return this.NotFound(), return this.BadRequest(..), ...
            // return StatusCode(400, default(string));
            string exampleJson = null;
            exampleJson = "{\n  \"identificationList\" : [ {\n    \"identifier\" : \"identifier\",\n    \"type\" : \"iso3\"\n  }, {\n    \"identifier\" : \"identifier\",\n    \"type\" : \"iso3\"\n  } ],\n  \"name\" : \"name\",\n  \"type\" : \"Cash\"\n}";
            
            var example = exampleJson != null
            ? JsonSerializer.Deserialize<FinancialInstrument>(exampleJson)
            : default(FinancialInstrument);
            //TODO: Change the data returned
            return new ObjectResult(example);
        }
    }
}